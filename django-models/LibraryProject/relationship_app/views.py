from django.http import HttpRequest
from django.shortcuts import render
from .models import Book, Library
from django.views import generic


# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}

    return render(request, "relationship_app/list_books.html", books)

class LibraryDetailView(generic.DetailView):
    model = Library
    template_name = "library_detail.html"
