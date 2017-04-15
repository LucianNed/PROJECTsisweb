from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Game, Platform, Region, Accesory
from views import GameDetail, PlatformDetail, PlatformGames

urlpatterns = [
    #List 5 newest games: /mygames/
    url(r'^$',
        ListView.as_view(
            queryset=Game.objects.order_by('date')[:5],
            context_object_name='latest_games_list',
            template_name='game_list.html'),
            name='game_list'),

    #games details, /mygames/games/1
    url(r'^games/(?P<pk>\d+)/$',
        GameDetail.as_view(),
        name='game_detail'),

    # list 5 platforms: /mygames/platforms/
    url(r'^platforms/all',
        ListView.as_view(
            queryset=Platform.objects.all,
            context_object_name='platform_list',
            template_name='platform_list.html'),
            name='platform_all',
        ),

    # platform details, /mygames/platforms/1
    url(r'^platforms/(?P<pk>\d+)/$',
        PlatformDetail.as_view(),
        name='platform_detail'
        ),

    # games for this platform, /mygames/platforms/1/games
    url(r'^platforms/(?P<pk>\d+)/games/$',
        PlatformGames.as_view(
            model= Accesory,
            template_name= 'platform_games.html'),
            name='platform_games'),

    # accessories for this platform, /mygames/platforms/1/games
    url(r'^platforms/(?P<pk>\d+)/accesories/$',
        ListView.as_view(
            queryset=Accesory.objects.filter(name__contains='a').order_by('name')[:5],
            context_object_name='platform_accesory_list',
            template_name='platform_accessories.html'),
            name='platform_accessories'),

    #to be contineud

]




