# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from models import Game, Platform, Accesory, Region
from django.http import HttpResponse, Http404

def homepage(request):
    return render_to_response("base.html", {
        'title': 'myGames',
        'content': 'Information about Video Games',
        'author': 'Anonimous'
    }, )


class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        return context


class PlatformDetail(DetailView):
    model = Platform
    template_name = 'platform_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformDetail, self).get_context_data(**kwargs)
        context['P_GAMES'] = Game.objects.filter(platform=self.kwargs.get('pk'))
        context['P_ACCESSORIES'] = Accesory.objects.filter(platform=self.kwargs.get('pk'))
        return context


class AccesoryDetail(DetailView):
    model = Accesory
    template_name = 'accesory_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AccesoryDetail, self).get_context_data(**kwargs)
        return context
