from django.urls import path
from .views import LibraryDetailView, list_books


urlpatterns = [
    path("", list_books, name="book list"),
    path("<int:pk>/library", LibraryDetailView.as_view(), name="detail")
]
