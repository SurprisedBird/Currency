import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver

from accounts.models import User


# хорошая практика - разделять receiverы и делать отдельный для каждого запроса. НЕ ВЫЗЫВАТЬ МЕТОД save() = циклическая рекурсия
@receiver(pre_save, sender=User)
def update_user_phone(sender, instance, **kwargs):
    if instance.phone:
        instance.phone = ''.join(char for char in instance.phone if char.isdigit())


@receiver(pre_save, sender=User)
def set_user_phone(sender, instance, **kwargs):
    if not instance.username:
        instance.username = str(uuid.uuid4)


@receiver(pre_save, sender=User)
def update_user_phone(sender, instance, **kwargs):
    print("AFTER")
