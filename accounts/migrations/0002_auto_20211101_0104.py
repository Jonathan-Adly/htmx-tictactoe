# Generated by Django 3.2.8 on 2021-11-01 01:04

import accounts.models
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='board',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), default=accounts.models.CustomUser.get_default, size=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='player',
            field=models.CharField(default='X', max_length=1),
        ),
    ]
