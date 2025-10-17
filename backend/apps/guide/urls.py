from django.urls import path
from . import views

urlpatterns = [
    path("ask/", views.ask, name="ask"),
    path("chats/", views.get_user_chats, name="get_user_chats"),
    path("history/<int:chat_id>/", views.get_chat_history, name="get_chat_history"),

]

