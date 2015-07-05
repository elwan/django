# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_sms', models.CharField(max_length=200)),
                ('date_pu', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse_sms', models.CharField(max_length=160)),
                ('question', models.ForeignKey(to='msi_sva.Question')),
            ],
        ),
    ]
