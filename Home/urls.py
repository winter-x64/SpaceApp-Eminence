from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome),
    path("home/", views.home),
    path("aboutus/", views.aboutus),
    path("contactus/", views.contactus),
]
