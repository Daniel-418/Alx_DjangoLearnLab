from django.http import HttpRequest
from django.shortcuts import render
from .models import Book


# Create your views here.
def booklist(request):
    books = {"books" : Book.objects.all()}

    return render(request, "list_books.html", books)
