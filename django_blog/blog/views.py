from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from .forms import CommentForm, CustomUserCreationForm, PostForm, UserUpdateForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post

# Create your views here.
class UserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required(login_url=reverse_lazy("login"))
def UserUpdateView(request:HttpRequest):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

#Shows all the lists of posts
class PostListView(LoginRequiredMixin,
                   ListView):
    login_url = reverse_lazy("login")
    template_name = "blog/post_list.html"
    model = Post

#Shows a specific Post
class PostDetailView(LoginRequiredMixin,
                     DetailView):
    template_name = "blog/post.html"
    login_url = reverse_lazy("login")
    model = Post

#Creates a Post
class PostCreateView(LoginRequiredMixin,
                     CreateView):
    login_url = reverse_lazy("login")
    form_class = PostForm
    model = Post
    template_name = "blog/new_post.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

#Updates a specific post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):
    template_name = "blog/post_update.html"
    login_url = reverse_lazy("login")
    model = Post
    fields = ["title", "content"]

    def get_success_url(self) -> str:
        return reverse("post_detail", kwargs={"pk": self.object.pk })

    def test_func(self):
        post = self.get_object() # pyright: ignore
        return post.author == self.request.user

#Deletes a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     DeleteView):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("post_list")
    template_name = "blog/post_delete.html"
    model = Post

    def test_func(self):
        post = self.get_object() # pyright: ignore
        return post.author == self.request.user

#Shows all the list comments
class CommentListView(LoginRequiredMixin,
                   ListView):
    login_url = reverse_lazy("login")
    template_name = "blog/comment_list.html"
    model = Comment

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs["pk"])

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_post());

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["post"] = self.get_post()
        return context_data

#Shows a specific comment
class CommentDetailView(LoginRequiredMixin,
                     DetailView):
    template_name = "blog/comment.html"
    login_url = reverse_lazy("login")
    model = Comment
    pk_url_kwarg = "comment_pk"

#Creates a Post
class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    form_class = CommentForm
    template_name = "blog/new_comment.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("comment_list", kwargs={"pk": self.kwargs["pk"]})

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["post"] = self.get_post()
        return ctx;

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.post = self.get_post()
        obj.save()
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     UpdateView):
    template_name = "blog/comment_update.html"
    login_url = reverse_lazy("login")
    model = Comment
    fields = ["content"]
    pk_url_kwarg = "comment_pk"

    def get_success_url(self) -> str:
        return reverse("comment_detail", kwargs={"pk": self.object.post_id, "comment_pk": self.object.pk })

    def test_func(self):
        comment = self.get_object() # pyright: ignore
        return comment.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     DeleteView):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("_list")
    template_name = "blog/comment_delete.html"
    model = Comment
    pk_url_kwarg = "comment_pk"

    def get_success_url(self) -> str:
        return  reverse_lazy("comment_list", kwargs={"pk": self.kwargs["pk"]})

    def test_func(self):
        comment = self.get_object() # pyright: ignore
        return comment.author == self.request.user
