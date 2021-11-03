from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("change-player", views.change_player, name="change_player"),
    path("play", views.play, name="play"),
    path("reset", views.reset, name="reset"),
]
