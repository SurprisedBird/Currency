from django.db import models

from currency import model_choices


# Create your models here.
class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=2056, null=True)
    created = models.DateTimeField(auto_now=True)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=24, unique=True, editable=False)


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    buy = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(Source, related_name='rates', on_delete=models.CASCADE)
    curr_type = models.CharField(max_length=3, choices=model_choices.RATE_TYPES,
                                 blank=False, null=False, default=model_choices.TYPE_USD)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=225)
    response_time = models.PositiveSmallIntegerField(default=0)
    request_method = models.CharField(max_length=10, choices=model_choices.REQUEST_METHODS)
