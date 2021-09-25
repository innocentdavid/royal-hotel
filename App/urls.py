
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("allRooms", views.allRooms, name="allRooms"),
    path("booking", views.booking, name="booking"),
    path("profile", views.profile, name="profile"),

    path("getRooms", views.getRooms, name="getRooms"),
    path("getCatg", views.getCatg, name="getCatg"),
    
    path("login_view", views.login_view, name="login_view"),
    path("register_view", views.register_view, name="register_view"),
    path("logout_view", views.logout_view, name="logout_view"),
]
