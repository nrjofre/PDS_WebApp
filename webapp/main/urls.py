from atexit import register
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('homes/', views.Profile.as_view(), name="homes"),
    #path('homes/<home_id>', views.Home.as_view(), name="home devices"),
    path('register/', views.Register.as_view(), name="register"),
    path('', views.Index.as_view(), name="index")
]
