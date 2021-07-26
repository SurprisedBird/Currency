from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    text = models.CharField(max_length=300)


""" phone_number = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    file = models.FileField() """
