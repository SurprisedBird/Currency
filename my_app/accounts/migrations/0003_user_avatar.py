# Generated by Django 3.2.5 on 2021-09-24 13:26

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210914_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to=accounts.models.upload_avatar),
        ),
    ]
