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

    game = HyperlinkedRelatedField(many=True, read_only=True, view_name='mygames:game-detail')

    class Meta:
        model = Platform
        fields = ('uri', 'platform_name', 'manufacturer', 'game')
