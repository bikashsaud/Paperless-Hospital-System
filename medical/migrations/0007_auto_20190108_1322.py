# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-01-08 07:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0006_auto_20190108_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='join_date',
            field=models.DateField(null=True, verbose_name=datetime.datetime(2019, 1, 8, 7, 37, 35, 162727, tzinfo=utc)),
        ),
    ]
