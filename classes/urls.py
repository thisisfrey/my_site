from django.urls import path
from . import views

urlpatterns = [
    path("book-a-class", views.book_a_class, name="book-a-class"),
]
