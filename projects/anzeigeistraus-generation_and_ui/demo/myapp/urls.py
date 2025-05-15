from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process_query/', views.process_query, name='process_query'),
    path('chat_view/', views.chat_view, name='chat_view'),
    path('clear-chat-history/', views.clear_chat_history, name='clear_chat_history'),
]