from import_export import resources

from currency.models import Rate, ResponseLog, Source


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sale',
            'bank_name',
            'currency_name',
        )


class SourceResource(resources.ModelResource):

    class Meta:
        model = Rate
        fields = (
            'source_url',
            'name',
        )


class ResponseLogResource(resources.ModelResource):

    class Meta:
        model = ResponseLog
        fields = (
            'id',
            'created',
            'status_code',
            'path',
            'response_time',
            'request_method',
        )
