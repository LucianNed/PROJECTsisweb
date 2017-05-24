from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Game(models.Model):
    game_name = models.TextField(blank=True)
    genre = models.TextField()
    multiplayer = models.IntegerField(default=0)
    developer = models.TextField()
    publisher = models.TextField()

    def __unicode__(self):
        return u"%s" % self.game_name

    def get_absolute_url(self):
        return reverse('mygames:game_detail', kwargs={'pk': self.pk})


class Platform(models.Model):
    platform_name = models.TextField(blank=True)
    manufacturer = models.TextField(blank=True)
    games = models.ManyToManyField(Game)

    def __unicode__(self):
        return u"%s" % self.platform_name

    def get_absolute_url(self):
        return reverse('mygames:platform_detail', kwargs={'pk': self.pk})


class Region(models.Model):
    region_name = models.TextField(blank=True)
    STANDARD_CHOICES = ((1, 'PAL'),(2, 'NTSC-U'),(3, 'NTSC-J'),(4, 'NTSC-C'))
    tv_format = models.PositiveSmallIntegerField('format ', blank=False, default=1, choices=STANDARD_CHOICES)

    def __unicode__(self):
        return self.region_name

    def get_absolute_url(self):
        return reverse('mygames:region', kwargs={'pk': self.pk})


class Accesory(models.Model):
    name = models.TextField()
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    genre = models.TextField() #game genre

    def __unicode__(self):
        return self.name


class Release(models.Model):
    release_date = models.DateField(default=date.today())
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.release_date.strftime('%d/%m/%Y')


#2na practica
class Score(models.Model):
    RATING_CHOICES = ((0, 'zero'), (1, 'one'), (2, 'two'),
                      (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)',
                                              blank=False, default=3, choices=RATING_CHOICES)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class GameScore(Score):
    game = models.ForeignKey(Game)


class FavoriteGame(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.TextField(default="Pong")

    def __unicode__(self):
        return self.name
