from django.contrib import admin
from character.models import Player, Enemy

# Register your models here.
admin.site.register([Player, Enemy])
