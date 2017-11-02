# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-22 05:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=20, null=True, unique=True)),
                ('code', models.CharField(max_length=20, null=True, unique=True)),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
