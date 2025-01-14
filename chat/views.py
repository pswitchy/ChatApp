# chat/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from .models import ChatMessage, UserProfile
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator
from django.utils import timezone
import json
import os

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id)
    user_profile = request.user.userprofile
    user_profile.is_online = True
    user_profile.save()
    
    # Fetch current chat messages
    current_chat = ChatMessage.objects.filter(receiver=request.user).order_by('-timestamp')[:10]

    # Fetch notifications
    notifications = ChatMessage.objects.filter(receiver=request.user).order_by('-timestamp')[:10]

    return render(request, 'chat/home.html', {
        'users': users,
        'user_profile': user_profile,
        'current_chat': current_chat,
        'notifications': notifications,
    })

@login_required
def chat_room(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    messages = ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('timestamp')
    
    # Mark messages as read
    unread_messages = messages.filter(receiver=request.user, is_read=False)
    unread_messages.update(is_read=True)
    
    paginator = Paginator(messages, 50)  # Show 50 messages per page
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    
    return render(request, 'chat/room.html', {
        'other_user': other_user,
        'messages': messages,
        'room_name': f"chat_{min(request.user.id, user_id)}_{max(request.user.id, user_id)}"
    })

@login_required
def send_message(request, user_id):
    if request.method == 'POST':
        receiver = get_object_or_404(User, id=user_id)
        message = request.POST.get('message', '')
        attachment = request.FILES.get('attachment')
        
        chat_message = ChatMessage.objects.create(
            sender=request.user,
            receiver=receiver,
            message=message,
            attachment=attachment
        )
        
        return JsonResponse({
            'status': 'success',
            'message': 'Message sent successfully',
            'data': {
                'sender': request.user.username,
                'message': message,
                'timestamp': chat_message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'attachment': chat_message.attachment.url if chat_message.attachment else None
            }
        })
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat:chat_home')
        else:
            return render(request, 'chat/login.html', {'error': 'Invalid username or password'})
    return render(request, 'chat/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'chat/signup.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the backend
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('chat:chat_home')
    return render(request, 'chat/signup.html')

def logout_view(request):
    logout(request)
    return redirect('chat:login')

@login_required
def profile_view(request):
    # Fetch distinct users the current user has chatted with
    sent_chats = ChatMessage.objects.filter(sender=request.user).values('receiver').distinct()
    received_chats = ChatMessage.objects.filter(receiver=request.user).values('sender').distinct()
    
    # Combine and get unique users
    chat_users = set()
    for chat in sent_chats:
        chat_users.add(chat['receiver'])
    for chat in received_chats:
        chat_users.add(chat['sender'])
    
    # Prepare chat data
    chat_data = []
    for user_id in chat_users:
        other_user = User.objects.get(id=user_id)
        start_time = ChatMessage.objects.filter(
            (Q(sender=request.user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=request.user))
        ).order_by('timestamp').first().timestamp
        end_time = ChatMessage.objects.filter(
            (Q(sender=request.user) & Q(receiver=other_user)) |
            (Q(sender=other_user) & Q(receiver=request.user))
        ).order_by('-timestamp').first().timestamp
        chat_data.append({
            'other_user': other_user,
            'start_time': start_time,
            'end_time': end_time,
        })
    
    return render(request, 'chat/profile.html', {
        'chats': chat_data,
    })

def add_numbers_view(request):
    # Dummy implementation for add_numbers_view
    result = {'result': 8}  # Example result
    return JsonResponse(result)

def upload_file_view(request):
    # Dummy implementation for upload_file_view
    result = {'message': 'File uploaded successfully'}
    return JsonResponse(result)

@login_required
def home(request):
    return render(request, 'chat/home.html')