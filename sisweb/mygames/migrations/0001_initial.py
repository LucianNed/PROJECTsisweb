# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-26 19:38
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('genre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='Pong')),
                ('created', models.DateField(default=datetime.date.today)),
                ('updated', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.TextField(blank=True)),
                ('genre', models.TextField()),
                ('multiplayer', models.IntegerField(default=0)),
                ('developer', models.TextField()),
                ('publisher', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')], default=3, verbose_name='Rating (stars)')),
                ('date', models.DateField(default=datetime.date.today)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Game')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.TextField(blank=True)),
                ('manufacturer', models.TextField(blank=True)),
                ('games', models.ManyToManyField(to='mygames.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.TextField(blank=True)),
                ('tv_format', models.PositiveSmallIntegerField(choices=[(1, 'PAL'), (2, 'NTSC-U'), (3, 'NTSC-J'), (4, 'NTSC-C')], default=1, verbose_name='format ')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField(default=datetime.date(2017, 5, 26))),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Platform')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Region')),
            ],
        ),
        migrations.AddField(
            model_name='accesory',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mygames.Platform'),
        ),
    ]
