from currency.models import ContactUs, Rate
from django_filters import rest_framework as filters
from rest_framework import fields


class RateFilter(filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('lt', 'lte', 'gt', 'gte', 'exact'),
            'sale': ('lt', 'lte', 'gt', 'gte', 'exact'),
            # 'type': ('in', ),
            # 'created': ('date', 'lte', 'gte'),
        }


class ContactUsFilter(filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {'email_to': ('exact', 'istartswith'),
                  'subject': ('exact', 'istartswith'),
                  'body': ('exact', 'istartswith'),
                  'created': ('date', 'lte', 'gte'), }
