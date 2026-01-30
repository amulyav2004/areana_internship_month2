from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('user/<str:username>/', views.profile_view_external, name='profile_view_external'),
    path('search/', views.search_view, name='search'),
]
