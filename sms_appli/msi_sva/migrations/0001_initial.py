# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-06 15:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campagne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('date_creation', models.DateTimeField()),
                ('nombre_total_vote', models.IntegerField(default=0)),
                ('date_campagne', models.DateTimeField(auto_now_add=True, verbose_name='Date creation')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categorie', models.CharField(max_length=100, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dictionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mot', models.CharField(max_length=10, unique=True)),
                ('definition', models.CharField(max_length=50)),
                ('synonyme', models.CharField(max_length=20)),
                ('antonyme', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('nom', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Nom Service')),
                ('adresse', models.CharField(max_length=50, verbose_name='Adresse')),
                ('telephone_mobile', models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.", regex='^7\\d{8}$')], verbose_name='Mobile')),
                ('telephone_fixe', models.CharField(blank=True, max_length=9, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '3xxxxxxxx'. Up to 9 digits allowed.", regex='^3\\d{8}$')], verbose_name='Telephone Fixe')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('site_web', models.URLField(blank=True, max_length=50, verbose_name='Site web')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
                ('tagline', models.TextField(blank=True, max_length=255, verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_sms', models.CharField(max_length=200, unique=True, verbose_name='Question')),
                ('date_pub', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='Dakar', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reponse_sms', models.CharField(max_length=160, verbose_name='Reponse')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Question', verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='Sms_recu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('message_text', models.CharField(max_length=160)),
                ('id_message', models.IntegerField()),
                ('numero_court', models.IntegerField()),
                ('date_reception', models.CharField(max_length=10)),
                ('date_enregistrement', models.DateTimeField(auto_now_add=True)),
                ('mot_cle', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_sous_categorie', models.CharField(max_length=100, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='date creation')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_candidat', models.CharField(max_length=20, unique=True)),
                ('id_candidat', models.CharField(max_length=5, unique=True)),
                ('votes', models.IntegerField(default=0)),
                ('date_vote', models.DateTimeField(auto_now_add=True, verbose_name='Date creation ')),
                ('campagne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Campagne')),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.SousCategorie', verbose_name='Caterogie de service'),
        ),
        migrations.AddField(
            model_name='info',
            name='localisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Commune'),
        ),
        migrations.AddField(
            model_name='departement',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Region'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msi_sva.Departement'),
        ),
    ]
