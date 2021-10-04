from currency import model_choices
from currency.models import ContactUs, Rate, Source
from currency.tasks import contact_us
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
            'curr_type',
            'source_obj',  # GET
            'source',  # POST
            'created',
        )
        extra_kwargs = {
            'source': {'write_only': True},
        }


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('email_to',
                  'subject',
                  'body',
                  'created',)

    def create(self, validated_data):
        subject = validated_data['subject']
        email_to = validated_data['email_to'],
        body = validated_data['body']

        contact_us.apply_async(kwargs={'subject': email_to, 'body': body})

        return ContactUs.objects.create(**validated_data)
