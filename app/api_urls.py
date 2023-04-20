from django.urls import path
from app import api
from rest_framework import routers
from .api import PlayerViewSet


router = routers.DefaultRouter()

router.register('api/players', PlayerViewSet, 'players')

api_urlpatterns = [
    path('api/login/', api.user_login, name='api-login')
]
