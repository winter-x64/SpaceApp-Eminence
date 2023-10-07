from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("authuser/", include("AuthUser.urls")),
    path("", include("Home.urls")),
]
