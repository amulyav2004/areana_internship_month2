from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Conversation, Message
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def inbox(request):
    conversations = request.user.conversations.all().order_by('-created_at')
    return render(request, 'chat/inbox.html', {'conversations': conversations})

@login_required
def chat_window(request, username):
    other_user = get_object_or_404(User, username=username)
    if other_user == request.user:
        return redirect('inbox')
    
    # Get or create conversation
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
    
    messages = conversation.messages.all()
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content
            )
            return redirect('chat_window', username=username)
            
    return render(request, 'chat/chat_window.html', {
        'conversation': conversation,
        'other_user': other_user,
        'messages': messages
    })
