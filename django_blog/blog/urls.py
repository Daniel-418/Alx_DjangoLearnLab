from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import UserCreationView, UserUpdateView
urlpatterns = [
    path("register/", UserCreationView.as_view(),
         name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"),
         name="login"),
    path("profile", UserUpdateView, name="profile")
]
