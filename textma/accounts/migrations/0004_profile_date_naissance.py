# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 21:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_profile_date_naissance'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2016, 6, 26, 21, 13, 3, 945267, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
