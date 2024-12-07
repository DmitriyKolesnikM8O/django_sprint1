from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]