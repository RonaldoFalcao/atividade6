
from django.contrib import admin
from django.urls import path
from aap1 import views

urlpatterns = [
    path('', views.home, name= "home"),
]
