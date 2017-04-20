from django.conf.urls import url
from django.views.generic import ListView
from models import Game, Platform, Region
from views import GameDetail, PlatformDetail, AccesoryDetail, RegionDetail, ReleaseDetail

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

    # list 5 platforms: /mygames/regions/
    url(r'^regions/$',
        ListView.as_view(
            queryset=Region.objects.all,
            context_object_name='region_list',
            template_name='region_list.html'),
            name='region_all',
        ),

    # platform details, /mygames/regions/1
    url(r'^regions/(?P<pk>\d+)/$',
        RegionDetail.as_view(),
        name='region_detail'
        ),

    # releases details /mygames/releases/1/games
    url(r'^releases/(?P<pk>\d+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),

    #to be contineud

]




