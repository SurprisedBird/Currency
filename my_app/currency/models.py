from django.db import models


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
    curr_type = models.CharField(max_length=3)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
