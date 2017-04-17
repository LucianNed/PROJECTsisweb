from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Game, Platform, Region, Accesory
from views import GameDetail, PlatformDetail, AccesoryDetail

urlpatterns = [
    #List 5 newest games: /mygames/
    url(r'^$',
        ListView.as_view(
            queryset=Game.objects.all(),
            context_object_name='latest_game_list',
            template_name='game_list.html'),
            name='game_list'),

    #games details, /mygames/games/1
    url(r'^games/(?P<pk>\d+)/$',
        GameDetail.as_view(),
        name='game_detail'),

    # list 5 platforms: /mygames/platforms/
    url(r'^platforms/$',
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

    # accessories details /mygames/accessories/1/games
    url(r'^accessories/(?P<pk>\d+)/$',
        AccesoryDetail.as_view(),
           name = 'accesory_detail'),

    #to be contineud

]




