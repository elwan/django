# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msi_sva', '0002_auto_20150705_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('nom', models.CharField(serialize=False, primary_key=True, max_length=20)),
                ('adresse', models.CharField(max_length=50)),
                ('telephone_mobile', models.IntegerField()),
                ('telephone_fixe', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nom_sous_categorie', models.CharField(max_length=100)),
                ('date_creation', models.DateTimeField(verbose_name='date creation')),
            ],
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
        migrations.RemoveField(
            model_name='infos',
            name='localisation',
        ),
        migrations.RemoveField(
            model_name='souscategories',
            name='categorie',
        ),
        migrations.DeleteModel(
            name='Infos',
        ),
        migrations.DeleteModel(
            name='SousCategories',
        ),
        migrations.AddField(
            model_name='souscategorie',
            name='categorie',
            field=models.ForeignKey(to='msi_sva.Categorie'),
        ),
        migrations.AddField(
            model_name='info',
            name='categorie',
            field=models.ForeignKey(to='msi_sva.SousCategorie'),
        ),
        migrations.AddField(
            model_name='info',
            name='localisation',
            field=models.ForeignKey(to='msi_sva.Localisation'),
        ),
    ]
