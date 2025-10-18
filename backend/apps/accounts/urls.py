from django.urls import path
from .views import register, login, current_user


urlpatterns = [
    path("register/", register, name="register"),
    path("users/", login, name="login"),
    path("current/", current_user, name="current-user"),
]
