
# chat/admin.py
from django.contrib import admin
from .models import ChatMessage, UserProfile

admin.site.register(ChatMessage)
admin.site.register(UserProfile)
