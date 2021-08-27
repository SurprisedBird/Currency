from celery import shared_task
from django.core.mail import send_mail
from settings import settings


@shared_task
def debug_task():
    print('My first Celery task')


@shared_task
def contact_us(subject, body):
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        ['irinayavors@gmail.com'],
        fail_silently=False,
    )
