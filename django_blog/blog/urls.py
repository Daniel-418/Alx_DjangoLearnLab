from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, UserCreationView, UserUpdateView

urlpatterns = [
    path("register/", UserCreationView.as_view(),
         name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"),
         name="login"),
    path("profile/", UserUpdateView, name="profile"),
    path("posts/new/", PostCreateView.as_view(), name="new_post"),
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="update_post"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="delete_post"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
