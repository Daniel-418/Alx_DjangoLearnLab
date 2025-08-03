from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views
from .views import SignUpView
from .views import librarian_view, admin_view, member_view


urlpatterns = [
    path("", list_books, name="book list"),
    path("<int:pk>/library", LibraryDetailView.as_view(), name="detail"),
    path("account/login",
         views.LoginView.as_view(template_name="relationship_app/login.html"),
         name="login"),
    path("account/register",
         SignUpView.as_view(), name='views.register'),
    path("account/logout", views.LogoutView.as_view(template_name="relationship_app/logout.html")),
    path("/account/admin", admin_view, name="admin view"),
    path("/account/librarian", librarian_view, name="librarian_view"),
    path("/account/member", member_view, name="member_view")
]
