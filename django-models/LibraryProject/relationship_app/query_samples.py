from django.db import models
from .models import Author, Librarian, Book, Library

author = Author.objects.get(name="Author_name")
author.book_set.all()

lib = Library.objects.get(name="Library_name")
books = lib.books.all()

lib = Library.objects.get(name="Library_name")
librarian = lib.librarian
