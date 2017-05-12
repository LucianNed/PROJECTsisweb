# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from models import *
from django.contrib.auth import authenticate
from forms import *


def Homepage(request):

    return render(request, "base.html", {
        'info': 'Information about Video Games',
        'user': request.user }, )


@csrf_exempt
def RegisterUser(request):
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


def RateGame(request, pk):
    game_r = get_object_or_404(Game, pk=pk)
    user_r = request.user
    rating = GameScore(
        rating=request.POST['rating'],
        user=user_r,
        game=game_r, )
    rating.save()
    return HttpResponseRedirect(reverse('mygames:game_detail', args=(game_r.id,)))


class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = GameScore.RATING_CHOICES
        context['G_SCORE'] = GameScore.objects.filter(game=self.kwargs.get('pk'))
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


class RegionDetail(DetailView):
    model = Region
    template_name = 'region_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RegionDetail, self).get_context_data(**kwargs)
        return context

class ReleaseDetail(DetailView):
    model = Release
    template_name = 'release_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ReleaseDetail, self).get_context_data(**kwargs)
        return context
