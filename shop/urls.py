from django.urls import path
from shop import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('buy/<str:weapon_id>', views.buy, name='shop-buy'),
    path('sell/<str:weapon_id>', views.sell, name='shop-sell'),
]
