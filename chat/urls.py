from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<str:username>/', views.chat_window, name='chat_window'),
]
