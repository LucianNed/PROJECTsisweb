# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from models import Game, Platform
from django.http import HttpResponse, Http404

def index(request):
    return HttpResponse("<h2>HOLAAAAAAA!!!!!</h2>")

def homepage(request):
    return render_to_response("homepage.html", {
        'title': 'myGames',
        'content': 'A shitty game thing web app',
        'author': 'Anonimous'
    }, )


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
