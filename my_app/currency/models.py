from django.db import models

from currency import model_choices


# Create your models here.
class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255, null=True)
    body = models.CharField(max_length=2056, null=True)
    created = models.DateTimeField(auto_now=True)


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    buy = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    curr_type = models.CharField(max_length=3, choices=model_choices.RATE_TYPES)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=225)
    response_time = models.PositiveSmallIntegerField(default=0)
    request_method = models.CharField(max_length=10, choices=model_choices.REQUEST_METHODS)
