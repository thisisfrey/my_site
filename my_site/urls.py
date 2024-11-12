"""
URL configuration for my_site project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("", include("classes.urls"))
]
