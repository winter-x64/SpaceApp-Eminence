from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Home.urls")),
    # path("auth/", include("AuthUser.urls")),
    # path("chat/", include("ChatApp.urls")),
    path("user/", include("users.urls")),
]
