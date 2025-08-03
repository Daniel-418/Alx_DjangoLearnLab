from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from .forms import BookForm

# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}

    return render(request, "relationship_app/list_books.html", books)

# Creates a book
@permission_required("relationship_app.can_add_books")
def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        else:
            form = BookForm()
    return render(request, "relationship_app.add_book.html", {"form": form})

# Deletes a book
@permission_required("relationship_app.can_delete_books")
def delete_book(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        if title and author:
            book = Book.objects.filter(title=title, author=author).first()
            if book:
                book.delete()
                return redirect("book_list")
            else:
                return HttpResponse("Book not found", status=400)
        else:
            return HttpResponse("invalid input", status=200)
    return render(request, "delete_book.html")

#Edits a book
@permission_required("relationship_app.can_change_book")
def change_book(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        new_title = request.POST.get("new_title")
        new_author = request.POST.get("new_author")
        if title and author:
            book = Book.objects.filter(title=title, author=author).first()
            if book:
                book.title = new_title
                book.author = new_author
                book.save()
                return redirect("book_list")
            else:
                return HttpResponse("Book not found", status=400)
        else:
            return HttpResponse("invalid input", status=200)
    return render(request, "edit_book.html")
            
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
