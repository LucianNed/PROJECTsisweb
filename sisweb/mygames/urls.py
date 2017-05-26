from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from models import *
from views import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns


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

    # accessories details /mygames/accessories/1
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

    # releases details /mygames/releases/1
    url(r'^releases/(?P<pk>\d+)/$',
        ReleaseDetail.as_view(),
        name='release_detail'),

    # give a game a rating, ex.: /mygames/games/1/ratings/create/
    url(r'^games/(?P<pk>\d+)/ratings/create/$',
        csrf_exempt(RateGame),
        name='rating_create'),

    # delete a game rating, ex.: /mygames/games/1/ratings/delete/
    url(r'^games/(?P<pk>\d+)/ratings/delete/$',
        csrf_exempt(DeleteRating),
        name='rating_delete')

]

# RESTful API
urlpatterns += [
    url(r'^api/games/$',
        APIGameList.as_view(), name='game-list'),
    url(r'^api/games/(?P<pk>\d+)/$',
        APIGameDetail.as_view(), name='game-detail'),
    url(r'^api/platforms/$',
        login_required(APIPlatformList.as_view()), name='platform-list'),
    url(r'^api/platforms/(?P<pk>\d+)/$',
        APIPlatformDetail.as_view(), name='platform-detail'),
    url(r'^api/accesories/$',
        login_required(APIAccesoryList.as_view()), name='accesory-list'),
    url(r'^api/accesories/(?P<pk>\d+)/$',
        APIAccesoryDetail.as_view(), name='accesory-detail'),
    url(r'^api/regions/$',
        login_required(APIRegionList.as_view()), name='region-list'),
    url(r'^api/regions/(?P<pk>\d+)/$',
        APIRegionDetail.as_view(), name='region-detail'),
    url(r'^api/gamescores/$',
        login_required(APIGamescoreList.as_view()), name='gamescore-list'),
    url(r'^api/gamescores/(?P<pk>\d+)/$',
        APIGamescoreDetail.as_view(), name='gamescore-detail'),
    url(r'^api/favorites/$',
        login_required(APIFavoriteList.as_view()), name='favoritegame-list'),
    url(r'^api/favorites/(?P<pk>\d+)/$',
        APIFavoriteDetail.as_view(), name='favoritegame-detail'),
    url(r'^api/releases/$',
        login_required(APIReleaseList.as_view()), name='release-list'),
    url(r'^api/releases/(?P<pk>\d+)/$',
        APIReleaseDetail.as_view(), name='release-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])
