from django.urls import path
from django.views.generic import DetailView
from .views import (ListView, UpdateView,
                    DeleteView, CreateView,
                    DetailView)

urlpatterns = [
    path("books/", ListView.as_view(), name="list"),
    path("books/<int:pk>/", DetailView.as_view(), name="detail"),
    path("books/update/<int:pk>", UpdateView.as_view(), name="update"),
    path("books/create/", CreateView.as_view(), name="create",),
    path("books/delete/<int:pk>", DeleteView.as_view(), name="delete")
]
