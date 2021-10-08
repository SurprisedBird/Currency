from decimal import Decimal

import requests
from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from settings import settings

from currency import consts, model_choices
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
    avilable_currency_types = {'USD': model_choices.TYPE_USD, 'EUR': model_choices.TYPE_EUR}
    response.raise_for_status()

    rates = response.json()
    source = Source.objects.get_or_create(code_name=consts.CODE_NAME_PRIVATBANK, defaults={'name': "privatbank"})[0]

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in avilable_currency_types:
            sale = Decimal(rate['sale']).quantize(Decimal(".01"))
            buy = Decimal(rate['buy']).quantize(Decimal(".01"))
            curr_type = avilable_currency_types[currency_type]

            last_rate = Rate.objects.filter(curr_type=curr_type, source=source).order_by("created").last()

            if last_rate is None or last_rate.sale != sale or last_rate.buy != buy:
                Rate.objects.create(curr_type=curr_type, sale=sale, buy=buy, source=source)

                cache.delete(consts.CACHE_KEY_LATEST_RATES)
                get_latest_rates()
