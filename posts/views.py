from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment, Like
from .forms import PostForm, CommentForm

@login_required
def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    posts = Post.objects.filter(is_archived=False)\
        .select_related('author', 'author__profile')\
        .prefetch_related('likes', 'comments')\
        .order_by('-created_at')
    return render(request, 'users/home.html', {'posts': posts, 'form': form})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'users/post_detail.html', {'post': post, 'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
        messages.success(request, "Post deleted successfully.")
    
    referer = request.META.get('HTTP_REFERER', '/')
    if f'/post/{post_id}/' in referer and 'delete' not in referer:
         return redirect('home')
    return redirect(referer)

@login_required
def archive_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.is_archived = True
        post.save()
        messages.success(request, "Post archived.")
    
    referer = request.META.get('HTTP_REFERER', 'home')
    return redirect(referer)

@login_required
def unarchive_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.is_archived = False
        post.save()
        messages.success(request, "Post unarchived.")
    
    referer = request.META.get('HTTP_REFERER', 'home')
    return redirect(referer)

@login_required
def archived_posts(request):
    posts = Post.objects.filter(author=request.user, is_archived=True)\
        .select_related('author', 'author__profile')\
        .prefetch_related('likes', 'comments')\
        .order_by('-created_at')
    return render(request, 'users/archived_posts.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(post=post, user=request.user)
    return redirect('home')
