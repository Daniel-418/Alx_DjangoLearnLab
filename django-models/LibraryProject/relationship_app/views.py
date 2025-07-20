from django.http import HttpRequest
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views import generic


# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}

    return render(request, "relationship_app/list_books.html", books)

class LibraryDetailView():
    model = Library
    template_name = "relationship_app/library_detail.html"
