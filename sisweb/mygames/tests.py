from django.contrib.auth.models import User
from django.test import TestCase
from models import *

class mygamesTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        game1 = Game.objects.create(game_name="game1")
        ptf1 = Platform.objects.create(platform_name="ptf")
        Accesory.objects.create(name='acc1', platform=ptf1, genre='genre')
        FavoriteGame.objects.create(user=user1, name="fvt1")
        GameScore.objects.create(rating=4, game=game1, user=user1)
        Region.objects.create(region_name="region1")

    def test_AccesoryCreation(self):
        acc1 = Accesory.objects.get(name='acc1')
        self.assertEquals(acc1.__unicode__(),acc1.name)

    def test_FavoriteCreation(self):
        ftv1 = FavoriteGame.objects.get(name="fvt1")
        self.assertEquals(ftv1.__unicode__(),ftv1.name)

    def test_RegionCreation(self):
        region = Region.objects.get(region_name="region1")
        self.assertEquals(region.__unicode__(),region.region_name)