# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-08 18:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveapplication', '0018_auto_20180108_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 8, 23, 53, 34, 844000)),
        ),
    ]
