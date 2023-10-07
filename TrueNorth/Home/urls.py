from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome),
    path("aboutus/", views.aboutus),
    path("contactus/", views.contactus),
]
