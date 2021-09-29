from currency.models import Rate
from rest_framework import serializers


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('sale', 'buy', 'source', 'curr_type', 'created')