# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 17:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursefavs', '0005_auto_20180228_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_added',
            field=models.DateTimeField(default=datetime.date(2018, 2, 28)),
        ),
    ]
