from currency.models import Rate, Source
from rest_framework import serializers


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
        )


class RateSerializer(serializers.ModelSerializer):
    source_obj = SourceSerializer(source='source', read_only=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'source',
            'type',
            'source_obj',  # GET
            'source',  # POST
            'created',
        )
        extra_kwargs = {
            'source': {'write_only': True},
        }
