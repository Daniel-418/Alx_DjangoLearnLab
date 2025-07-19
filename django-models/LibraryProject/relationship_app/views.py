from django.http import HttpRequest
from django.shortcuts import render
from .models import Book


# Create your views here.
def list_books(request):
    books = {"books" : Book.objects.all()}

    return render(request, "relationship_app/list_books.html", books)
