# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 21:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_date_naissance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_naissance',
        ),
    ]
