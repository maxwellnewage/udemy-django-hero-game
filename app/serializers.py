from rest_framework.serializers import ModelSerializer

from app.models import User
from character.models import Player


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_author']


class PlayerSerializer(ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ['id', 'name', 'hp', 'money', 'score', 'owner']
        depth = 1
