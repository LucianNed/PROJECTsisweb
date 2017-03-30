# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mygames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('intended_for', models.TextField()),
                ('for_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Platform')),
            ],
        ),
    ]
