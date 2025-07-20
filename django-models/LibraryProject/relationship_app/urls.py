from django.urls import path
from .views import list_books
from .views import LibraryDetailView


urlpatterns = [
    path("", list_books, name="book list"),
    path("<int:pk>/library", LibraryDetailView.as_view(), name="detail")
]
