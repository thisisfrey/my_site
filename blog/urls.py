from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts"),
    path("post/<slug:slug>", views.post, name="post")
]