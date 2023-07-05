from django.urls import path, re_path
from .views import dashboard_view, chat_view, notebook_view, chat_delete_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('chat/', chat_view, name='chat'),
    path('notebook/', notebook_view, name='notebook'),
    path('chat_delete/', chat_delete_view, name='chat_delete'),
]