# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-17 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='target_station_id',
            new_name='station_id',
        ),
    ]