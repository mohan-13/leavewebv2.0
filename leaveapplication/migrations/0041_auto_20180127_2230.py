# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-27 17:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0040_auto_20180127_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='from_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 27, 22, 30, 18, 240079)),
        ),
        migrations.AlterField(
            model_name='students',
            name='to_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 1, 27, 22, 30, 18, 241079)),
        ),
    ]
