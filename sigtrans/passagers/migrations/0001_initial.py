# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comptabilite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Passager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=100)),
                ('telephone', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
                ('prix_transport', models.IntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagers.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='TypeVehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('nombre_place', models.IntegerField(default=1)),
                ('poids_vehicule_vide', models.IntegerField(default=1)),
                ('poids_vehicule_charge', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagers.TypeVehicule')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('numero', models.IntegerField()),
                ('destination', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='passagers.Destination')),
                ('passager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagers.Passager')),
                ('vehicule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passagers.Vehicule')),
            ],
        ),
    ]
