from django.db import models
from .models import Author, Librarian, Book, Library
library_name = "Prince Albert Library"

author = Author.objects.get(name=Author_name)
author.book_set.all()

lib = Library.objects.get(name=library_name)
books = lib.books.all()

lib = Library.objects.get(name=library_name)
librarian = lib.librarian
