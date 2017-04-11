from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Game(models.Model):
    game_id = models.AutoField(primary_key=True, default=1)
    game_name = models.TextField(blank=True)
    genre = models.TextField()
    multiplayer = models.IntegerField(default=0)
    developer = models.TextField()
    publisher = models.TextField()
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.game_name
    def get_absolute_url(self):
        return reverse('mygames:game_detail', kwargs={'pk': self.pk})


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True, default=1)
    platform_name = models.TextField(blank=True)
    manufacturer = models.TextField(blank=True)
    games = models.ManyToManyField(Game)

    def __unicode__(self):
        return u"%s" % self.platform_name
    def get_absolute_url(self):
        return  reverse('mygames:platform_detail', kwargs={'pk': self.pk})


class Region(models.Model):
    region_id = models.AutoField(primary_key=True, default=1)
    region_name = models.TextField(blank=True)
    STANDARD_CHOICES = ((1, 'PAL'),(2, 'NTSC-U'),(3, 'NTSC-J'),(4, 'NTSC-C'))
    format = models.PositiveSmallIntegerField('format ', blank=False, default=1, choices=STANDARD_CHOICES)


class Accesory(models.Model):
    name = models.TextField()
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    genre = models.TextField() #game genre


class Release(Game, Platform, Region):
    release_date = models.DateField(default=date.today())


#2na practica
class UserRating(Game, User):
    RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)

    def __unicode__(self):
        return u"%d" % self.rating
