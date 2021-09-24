# Generated by Django 3.2.5 on 2021-09-24 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_to', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255, null=True)),
                ('body', models.CharField(max_length=2056, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.PositiveSmallIntegerField()),
                ('path', models.CharField(max_length=225)),
                ('response_time', models.PositiveSmallIntegerField(default=0)),
                ('request_method', models.CharField(choices=[('GET', 'GET method'), ('POST', 'POSR method')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=64)),
                ('code_name', models.CharField(editable=False, max_length=24, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('buy', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('curr_type', models.CharField(choices=[('USD', 'Dollar'), ('EUR', 'Euro')], default='USD', max_length=3)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.source')),
            ],
        ),
    ]
