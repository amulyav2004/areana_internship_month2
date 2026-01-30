from django.contrib import admin
from .models import CustomUser, Profile
from posts.models import Post, Comment, Like
from friends.models import Follow

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)
