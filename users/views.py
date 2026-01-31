from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import CustomUserCreationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def profile_view(request):
    from posts.models import Post
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    posts = Post.objects.filter(author=request.user, is_archived=False).order_by('-created_at')
    context = {
        'p_form': p_form,
        'posts': posts,
        'profile_user': request.user
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_view_external(request, username):
    from posts.models import Post
    from friends.models import Follow
    profile_user = get_object_or_404(User, username=username)
    if profile_user == request.user:
        return redirect('profile')
    
    posts = Post.objects.filter(author=profile_user, is_archived=False).order_by('-created_at')
    is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    
    can_view = not profile_user.profile.is_private or is_following or profile_user == request.user

    context = {
        'profile_user': profile_user,
        'posts': posts if can_view else [],
        'is_following': is_following,
        'can_view': can_view
    }
    return render(request, 'users/profile_external.html', context)

@login_required
def search_view(request):
    from posts.models import Post
    query = request.GET.get('q', '')
    users = []
    posts = []
    if query:
        # Search for users by username or bio
        users = User.objects.filter(
            Q(username__icontains=query) | Q(profile__bio__icontains=query)
        ).select_related('profile').distinct()
        
        # Search for posts by content or author's username
        posts = Post.objects.filter(
            (Q(content__icontains=query) | Q(author__username__icontains=query)) & 
            Q(is_archived=False)
        ).select_related('author', 'author__profile')\
         .prefetch_related('likes', 'comments')\
         .order_by('-created_at')
    
    return render(request, 'users/search_results.html', {
        'users': users,
        'posts': posts,
        'query': query
    })
