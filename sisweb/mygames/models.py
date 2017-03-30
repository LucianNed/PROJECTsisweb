from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from datetime import date

# Create your models here.

class Game(models.Model):
    name = models.TextField()
    genre = models.TextField()
    developer = models.TextField()
    publisher = models.TextField()
    date = models.DateField(default=date.today)
    #rating
    #to be continued ...

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('mygames:game_detail', kwargs={'pk': self.pk})

class Platform(models.Model):
    name = models.TextField(blank=True)
    manufacturer = models.TextField(blank=True)
    format = models.TextField(blank=True)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return  reverse('mygames:platform_detail', kwargs={'pk': self.pk})

class Region(models.Model):
    name = models.TextField(blank=True)
    standard = ((1, 'PAL'),(2, 'NTSC-U'),(3, 'NTSC-J'),(4, 'NTSC-C'))

    def __unicode__(self):
        return u"%s" % self.name

class Accesory(models.Model):
    name = models.TextField()
    for_device = models.ForeignKey('Platform', on_delete=models.CASCADE)
    intended_for = models.TextField() #game genre