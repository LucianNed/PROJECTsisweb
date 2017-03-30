from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from models import Game, Platform, Accesory

class GameDetail(DetailView):
    model = Game
    template_name = 'mygames/game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context


class PlatformDetail(DetailView):
    model = Platform
    template_name = 'mygames/platform_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        return context
