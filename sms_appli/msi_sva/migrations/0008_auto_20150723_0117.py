# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('msi_sva', '0007_auto_20150719_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='telephone_fixe',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(regex=b'^\\d{3,9}$', message=b"Phone number must be entered in the format: '3xxxxxxxx'. Up to 9 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='info',
            name='telephone_mobile',
            field=models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(regex=b'^\\d{7,9}$', message=b"Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")]),
        ),
    ]
