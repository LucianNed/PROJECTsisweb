# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from django.db.models import Avg
from models import *
from forms import *
from serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@csrf_exempt
def Homepage(request):
    if request.method == 'POST':
        user_f = request.user
        game_r = FavoriteGame.objects.filter(user=user_f)
        game_f = request.POST.get('favorite_game', "pong")
        if len(game_r) == 0:
            favorite = FavoriteGame(
                user=user_f,
                name=game_f, )
            favorite.save()
        else:
            game_r.update(name=game_f, updated=date.today())
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
    user_r = request.user
    game_r = get_object_or_404(Game, pk=pk)
    rate_f = GameScore.objects.filter(user=user_r)
    if len(rate_f) == 0:
        rating = GameScore(
            rating=request.POST['rating'],
            user=user_r,
            game=game_r, )
        rating.save()
    else:
        rate_f.update(rating=request.POST['rating'], date=date.today())
    return HttpResponseRedirect(reverse('mygames:game_detail', args=(game_r.id,)))


def DeleteRating(request, pk):
    rating = GameScore.objects.get(id=pk)
    game_r = rating.game
    rating.delete()
    return HttpResponseRedirect(reverse('mygames:game_detail', args=(game_r.id,)))


class GameDetail(DetailView):
    model = Game
    template_name = 'game_detail.html'

    def get_context_data(self, **kwargs):
        context = super(GameDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = GameScore.RATING_CHOICES
        context['G_SCORE'] = GameScore.objects.filter(game=self.kwargs.get('pk'))
        context['AVG_RATING'] = GameScore.objects.filter(game=self.kwargs.get('pk')).aggregate(Avg('rating'))
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


# API
class APIGameList(generics.ListAPIView):
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class APIGameDetail(generics.RetrieveAPIView):
    model = Game
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class APIPlatformList(generics.ListAPIView):
    model = Platform
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class APIPlatformDetail(generics.RetrieveAPIView):
    model = Platform
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class APIRegionList(generics.ListAPIView):
    model = Region
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class APIRegionDetail(generics.RetrieveAPIView):
    model = Region
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class APIAccesoryList(generics.ListAPIView):
    model = Accesory
    queryset = Accesory.objects.all()
    serializer_class = AccesorySerializer


class APIAccesoryDetail(generics.RetrieveAPIView):
    model = Accesory
    queryset = Accesory.objects.all()
    serializer_class = AccesorySerializer


class APIGamescoreList(generics.ListCreateAPIView):
    model = GameScore
    queryset = GameScore.objects.all()
    serializer_class = GamescoreSerializer


class APIGamescoreDetail(generics.RetrieveUpdateDestroyAPIView):
    model = GameScore
    queryset = GameScore.objects.all()
    serializer_class = GamescoreSerializer


class APIFavoriteList(generics.ListCreateAPIView):
    model = FavoriteGame
    queryset = FavoriteGame.objects.all()
    serializer_class = FavoriteSerializer


class APIFavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    model = FavoriteGame
    queryset = FavoriteGame.objects.all()
    serializer_class = FavoriteSerializer


class APIReleaseList(generics.ListAPIView):
    model = Release
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer


class APIReleaseDetail(generics.RetrieveAPIView):
    model = Release
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
