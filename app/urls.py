from django.urls import path
from app import views
from .api_urls import api_urlpatterns, router

urlpatterns = [
    path('', views.index, name="home"),

    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('logout/', views.user_logout, name="logout"),
]

urlpatterns += api_urlpatterns + router.urls
