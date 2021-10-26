import re
from datetime import date, timedelta
from decimal import Decimal

import numpy as np
import requests
from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from settings import settings

from currency import consts, model_choices
from currency.models import Source
from currency.services import get_latest_rates


@shared_task
def debug_task():
    # from currency.models import Rate
    # print(f'Count Rate {Rate.objects.count()}')
    print(' ')


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source
    privatbank_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(privatbank_url)
    available_currency_types = {'USD': model_choices.TYPE_USD, 'EUR': model_choices.TYPE_EUR}
    response.raise_for_status()

    rates = response.json()
    source = Source.objects.get_or_create(code_name=consts.CODE_NAME_PRIVATBANK, defaults={'name': "privatbank"})[0]

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:
            sale = Decimal(rate['sale']).quantize(Decimal(".01"))
            buy = Decimal(rate['buy']).quantize(Decimal(".01"))
            curr_type = available_currency_types[currency_type]

            last_rate = Rate.objects.filter(curr_type=curr_type, source=source).order_by("created").last()

            if last_rate is None or last_rate.sale != sale or last_rate.buy != buy:
                Rate.objects.create(curr_type=curr_type, sale=sale, buy=buy, source=source)

                cache.delete(consts.CACHE_KEY_LATEST_RATES)
                get_latest_rates()


@shared_task
def parse_privatbank_archive():
    from currency.models import Rate
    archive_url = 'https://api.privatbank.ua/p24api/exchange_rates?json'
    available_currency_types = {'USD': model_choices.TYPE_USD, 'EUR': model_choices.TYPE_EUR}
    source = Source.objects.get_or_create(code_name=consts.CODE_NAME_PRIVATBANK, defaults={'name': "privatbank"})[0]

    sdate = date(2014, 1, 1)   # start date
    edate = date.today()   # end date
    delta = edate - sdate       # as timedelta
    date_list = np.array([])

    for i in range(delta.days + 1):
        now_date = str(sdate + timedelta(days=i))
        date_list = np.append(date_list, re.sub(
            r'(\d{4})-(\d\d)-(\d\d)', r'\3.\2.\1', now_date))

    np.flipud(date_list)

    for day in date_list:
        payload = {'date': day}

        response = requests.get(archive_url, params=payload)
        try:
            response.raise_for_status()
        except:
            response.status_code
            continue

        rate = response.json()
        if ('baseCurrency' in rate) and (len(rate['exchangeRate']) != 0):
            for exchange_rate in rate['exchangeRate']:
                currency_type = exchange_rate['currency']

                if currency_type in available_currency_types:
                    created = re.sub(
                        r'(\d\d).(\d\d).(\d{4})', r'\3-\2-\1', day)
                    print(created)
                    sale = exchange_rate['saleRateNB']
                    buy = exchange_rate['purchaseRateNB']
                    Rate.objects.update_or_create(sale=sale, buy=buy, created=created,
                                                  source=source, curr_type=currency_type, defaults={'created': created, 'curr_type': currency_type})
