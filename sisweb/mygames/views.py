# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import DetailView
from models import Game, Platform, Accesory, Region
from forms import *


def homepage(request):
    return render_to_response("base.html", {
        'title': 'myGames',
        'content': 'Information about Video Games',
        'author': 'Anonimous'
    }, )


def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])

            return HttpResponseRedirect('/mygames/')
    else:
        form = RegisterForm()
    return render_to_response('registration/register.html', {'form': form}, RequestContext(request))


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


