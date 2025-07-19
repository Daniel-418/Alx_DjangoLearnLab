from django.urls import path
from .views import list_books

url_patterns = [
    path("", list_books, name="book list")
]
