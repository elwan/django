# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True, verbose_name='Mini url')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('nbre_acces', models.IntegerField(default=0)),
                ('pseudo', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Mini Url',
                'verbose_name_plural': 'Minis Url',
            },
        ),
    ]
