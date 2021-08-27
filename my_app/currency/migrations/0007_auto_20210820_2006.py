# Generated by Django 3.2.5 on 2021-08-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_rename_rateus_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email',
            new_name='email_to',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='text',
        ),
        migrations.AddField(
            model_name='contactus',
            name='body',
            field=models.CharField(max_length=2056, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]