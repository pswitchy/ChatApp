# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.chat_home, name='chat_home'),
    path('chat/<int:user_id>/', views.chat_room, name='chat_room'),
    path('send/<int:user_id>/', views.send_message, name='send_message'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('add-numbers/', views.add_numbers_view, name='add_numbers'),
    path('upload-file/', views.upload_file_view, name='upload_file'),
    path('signup/', views.signup_view, name='signup'),
]