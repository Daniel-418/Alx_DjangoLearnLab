from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, UserUpdateForm
from django.urls import reverse_lazy

# Create your views here.
class UserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

def UserUpdateView(request:HttpRequest):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "blog/profile.html", {"form": form})

