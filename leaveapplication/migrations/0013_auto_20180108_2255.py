# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-08 17:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0012_auto_20180108_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 8, 22, 55, 41, 752000)),
        ),
    ]
