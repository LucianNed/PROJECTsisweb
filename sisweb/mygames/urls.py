




from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Game, Platform, Region, Accesory
from views import GameDetail, PlatformDetail

urlpatterns = [
    #List 5 newest games: /mygames/
    url(r'^$',
        ListView.as_view(
            queryset=Game.objects.filter(date__lte=timezone.now()).order_by('date')[:5],
            context_object_name='latest_games_list',
            template_name='mygames/game_list.html'),
            name='game_list'),
    #games details, /mygames/games/1
    url(r'^games/(?P<pk>\d+)/$',
        GameDetail.as_view(),
        name='game_detail'),

    #platform details, /platforms/platforms/1
    url(r'^platforms/(?P<pk>\d+)/$',
        PlatformDetail.as_view(),
        name='platform_detail'
    )
    #to be contineud

]




