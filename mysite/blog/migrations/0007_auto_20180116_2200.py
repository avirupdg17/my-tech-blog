# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-16 16:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180116_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 16, 16, 30, 31, 89392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 16, 16, 30, 31, 89392, tzinfo=utc)),
        ),
    ]
