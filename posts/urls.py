from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/archive/', views.archive_post, name='archive_post'),
    path('post/<int:post_id>/unarchive/', views.unarchive_post, name='unarchive_post'),
    path('archived-posts/', views.archived_posts, name='archived_posts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
