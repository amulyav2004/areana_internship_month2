from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('unread-count/', views.unread_count, name='unread_count'),
    path('delete/<int:pk>/', views.delete_notification, name='delete_notification'),
]
