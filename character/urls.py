from django.urls import path
from character import views


urlpatterns = [
    path('', views.player_profile, name="player-profile"),
    path('create', views.create_player, name="create-player"),
    path('update/<str:player_id>', views.update_player, name="update-player"),
    path('delete/<str:player_id>', views.delete_player, name="delete-player"),
]
