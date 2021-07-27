from django.http import HttpResponse
from django.shortcuts import render

from currency.models import ContactUs, RateUs


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello world')


def get_contact_us(request):
    contacts = ContactUs.objects.all()

    context = {
        "contact_list": contacts
    }

    return render(request, "contact.html", context=context)


def rate_us(request):
    rate = RateUs.objects.all()

    context = {
        "rate_list": rate
    }

    return render(request, "rate.html", context=context)
