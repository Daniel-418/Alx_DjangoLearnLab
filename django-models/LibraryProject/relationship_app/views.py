from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}
    x = "UserCreationForm()"

    return render(request, "relationship_app/list_books.html", books)

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

def is_admin(user):
    return user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, template_name="relationship_app/admin_view.html")

def is_librarian(user):
    return user.userprofile.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, template_name="relationship_app/librarian_view.html")

def is_member(user):
    return user.userprofile.role == "Member"

@user_passes_test(is_member)
def member_view(request):
    return render(request, template_name="relationship_app/member_view.html")
