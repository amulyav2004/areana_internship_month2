from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Group, GroupPost
from .forms import GroupForm, GroupPostForm

@login_required
def group_list(request):
    groups = Group.objects.all().order_by('-created_at')
    return render(request, 'groups/group_list.html', {'groups': groups})

@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            group.members.add(request.user)
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm()
    return render(request, 'groups/create_group.html', {'form': form})

@login_required
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    posts = group.posts.all().order_by('-created_at')
    is_member = request.user in group.members.all()
    
    if request.method == 'POST' and is_member:
        form = GroupPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.group = group
            post.author = request.user
            post.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupPostForm()
    
    return render(request, 'groups/group_detail.html', {
        'group': group,
        'posts': posts,
        'is_member': is_member,
        'form': form
    })

@login_required
def join_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    group.members.add(request.user)
    return redirect('group_detail', group_id=group.id)

@login_required
def leave_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if group.admin != request.user:
        group.members.remove(request.user)
    return redirect('group_list')
