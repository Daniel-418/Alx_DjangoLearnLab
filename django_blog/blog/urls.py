from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (CommentCreateView, CommentDeleteView, CommentDetailView, CommentListView, 
                    CommentUpdateView, PostCreateView, 
                    PostDeleteView, PostDetailView, 
                    PostListView, PostUpdateView, 
                    UserCreationView, UserUpdateView)

urlpatterns = [
    path("register/", UserCreationView.as_view(),
         name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"),
         name="login"),
    path("profile/", UserUpdateView, name="profile"),
    path("post/new/", PostCreateView.as_view(), name="new_post"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="delete_post"),
    path("post/", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/comments/<int:comment_pk>/update/", CommentUpdateView.as_view(), name="update_comment"),
    path("post/<int:pk>/comments/<int:comment_pk>/delete", CommentDeleteView.as_view(), name="delete_comment"),
    path("post/<int:pk>/comments/", CommentListView.as_view(), name="comment_list"),
    path("post/<int:pk>/comments/<int:comment_pk>/", CommentDetailView.as_view(), name="comment_detail"),
    path("post/<int:pk>/comments/new", CommentCreateView.as_view(), name="new_comment"),
]
