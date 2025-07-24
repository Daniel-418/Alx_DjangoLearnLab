from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views
from .views import SignUpView

urlpatterns = [
    path("", list_books, name="book list"),
    path("<int:pk>/library", LibraryDetailView.as_view(), name="detail"),
    path("account/login",
         views.LoginView.as_view(template_name="relationship_app/login.html"),
         name="login"),
    path("account/register",
         SignUpView.as_view(), name='views.register'),
    path("account/logout", views.LogoutView.as_view(template_name="relationship_app/logout.html"))
]
