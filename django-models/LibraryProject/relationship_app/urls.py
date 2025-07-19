from django.urls import path
from .views import list_books

urlpatterns = [
    path("", list_books, name="book list")
]
