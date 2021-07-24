from django.http import HttpResponse
from django.shortcuts import render

from currency.models import ContactUs


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello world')


def get_contact_us(request):
    contactUs_objects = ContactUs.objects.all()
    result = []

    for item in contactUs_objects:
        result.append(
            f'From: {item.name}, Topic: {item.email}, Text: {item.text} <br> <br>'
        )

    return HttpResponse(result)
