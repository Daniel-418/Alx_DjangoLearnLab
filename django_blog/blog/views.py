from django.contrib.auth import login, mixins
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, PostCreateForm, UserUpdateForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

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
class PostListView(mixins.LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    template_name = "blog/post_list.html"
    model = Post

#Shows a specific Post
class PostDetailView(mixins.LoginRequiredMixin, DetailView):
    template_name = "blog/post.html"
    login_url = reverse_lazy("login")
    model = Post

#Creates a Post
class PostCreateView(mixins.LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("login")
    form_class = PostCreateForm
    template_name = "blog/new_post.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

#Updates a specific post
class PostUpdateView(mixins.LoginRequiredMixin, UpdateView):
    template_name = "blog/post_update.html"
    login_url = reverse_lazy("login")
    model = Post
    fields = ["title", "content"]

    def get_success_url(self) -> str:
        return reverse("post_detail", kwargs={"pk": self.object.pk })

#Deletes a post
class PostDeleteView(mixins.LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("post_list")
    template_name = "blog/post_delete.html"
    model = Post
