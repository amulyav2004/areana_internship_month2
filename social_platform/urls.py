from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
