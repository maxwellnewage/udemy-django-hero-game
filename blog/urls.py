from django.urls import path
from blog import views

urlpatterns = [
    path('all', views.posts, name="posts"),
    path('create', views.create_post, name="create-post"),
    path('update/<str:post_id>', views.update_post, name="update-post"),
    path('delete/<str:post_id>', views.delete_post, name="delete-post"),
]
