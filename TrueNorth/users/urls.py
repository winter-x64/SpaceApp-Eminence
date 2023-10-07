from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.dashboard),
    # path("home/", views),
    # path("home/", views),
]
