from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilter

from currency.models import ContactUs, Rate, Source
from currency.resources import RateResource, SourceResource


# Register your models here.
class RateAdmin(ImportExportModelAdmin):
    resourse_class = RateResource
    list_display = ('id', 'buy', 'sale', 'curr_type', 'source', 'created',)

    list_filter = ('curr_type',
                   ('created', DateRangeFilter), )

    search_fields = ('curr_type', 'source',)
    readonly_fields = ('sale', 'buy',)

    def has_add_permission(self, request):
        return False


class SourceAdmin(ImportExportModelAdmin):
    resourse_class = SourceResource
    list_display = ('id', 'source_url', 'name',)

    list_filter = ('source_url', )

    search_fields = ('name',)
    readonly_fields = ('source_url',)

    def has_add_permission(self, request):
        return False


class ContactUsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'email_to',
        'subject',
        'body',
        'created',
    )
    list_filter = (
        'id',
        ('created', DateRangeFilter),
    )
    search_fields = (
        'subject',
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Rate, RateAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
