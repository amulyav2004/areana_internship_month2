from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('users/', include('users.urls')),
    path('friends/', include('friends.urls')),
    path('notifications/', include('notifications.urls')),
    path('api/', include('api.urls')),
    path('chat/', include('chat.urls')),
    path('groups/', include('groups.urls')),
    path('events/', include('events.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serves media files in both dev and production
# Important for Render/Heroku where Nginx/Apache isn't managing media
urlpatterns += [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
]
