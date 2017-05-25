from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *


class GameSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:game-detail')

    platform_set = HyperlinkedRelatedField(many=True, read_only=True,
                                           view_name='mygames:platform-detail')

    class Meta:
        model = Game
        fields = ('uri', 'game_name', 'genre', 'multiplayer', 'developer', 'publisher', 'platform_set')


class PlatformSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:platform-detail')

    games = HyperlinkedRelatedField(many=True, read_only=True, view_name='mygames:game-detail')

    class Meta:
        model = Platform
        fields = ('uri', 'platform_name', 'manufacturer', 'games')


class RegionSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:region-detail')

    class Meta:
        model = Region
        fields = ('uri', 'region_name', 'tv_format')


class AccesorySerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:accesory-detail')

    platform = HyperlinkedRelatedField(read_only=True, view_name='mygames:platform-detail')

    class Meta:
        model = Accesory
        fields = ('uri', 'name', 'platform', 'genre')


class GamescoreSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:game-detail')

    game = HyperlinkedRelatedField(read_only=True, view_name='mygames:game-detail')
    user = CharField(read_only=True)

    class Meta:
        model = GameScore
        fields = ('uri', 'rating', 'user', 'date', 'game')


class FavoriteSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:game-detail')

    user = CharField(read_only=True)

    class Meta:
        model = FavoriteGame
        fields = ('uri', 'user', 'name')


class ReleaseSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='mygames:platform-detail')

    game = HyperlinkedRelatedField(read_only=True, view_name='mygames:game-detail')
    region = HyperlinkedRelatedField(many=True, read_only=True, view_name='mygames:region-detail')
    platform = HyperlinkedRelatedField(many=True, read_only=True, view_name='mygames:platform-detail')

    class Meta:
        model = Release
        fields = ('uri', 'game', 'platform', 'region', 'release_date')
