from django.urls import path
from arena import views

urlpatterns = [
    path('', views.home, name="arena"),
    path('attack/<str:enemy_id>', views.attack_enemy, name="arena-attack-enemy"),
]
