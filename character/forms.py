from django.forms import ModelForm
from character.models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['name']
