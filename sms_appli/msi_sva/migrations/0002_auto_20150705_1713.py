# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_sva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom_categorie', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('nom', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone_mobile', models.IntegerField()),
                ('telephone_fixe', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom_zone', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='SousCategories',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom_sous_categorie', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
                ('categorie', models.ForeignKey(to='msi_sva.Categories')),
            ],
        ),
        migrations.AddField(
            model_name='infos',
            name='localisation',
            field=models.ForeignKey(to='msi_sva.Localisation'),
        ),
    ]
