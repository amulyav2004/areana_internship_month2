from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Follow

User = get_user_model()

@login_required
def follow_user(request, user_id):
    to_follow = get_object_or_404(User, id=user_id)
    if to_follow != request.user:
        Follow.objects.get_or_create(follower=request.user, following=to_follow)
    return redirect('profile_view_external', username=to_follow.username)

@login_required
def unfollow_user(request, user_id):
    to_unfollow = get_object_or_404(User, id=user_id)
    Follow.objects.filter(follower=request.user, following=to_unfollow).delete()
    return redirect('profile_view_external', username=to_unfollow.username)
