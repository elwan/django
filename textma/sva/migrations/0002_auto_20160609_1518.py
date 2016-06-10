# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_erreur',
            name='msg_erreur_utilisateur',
            field=models.CharField(default='admin', max_length=20, verbose_name='Utilisateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message_erreur',
            name='msg_erreur_utilisateur_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reponse',
            name='reponse_utilisateur',
            field=models.CharField(default='admin', max_length=20, verbose_name='Utilisateur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reponse',
            name='reponse_utilisateur_id',
            field=models.IntegerField(default=0),
        ),
    ]
