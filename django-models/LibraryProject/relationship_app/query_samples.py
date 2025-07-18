from django.db import models
from .models import Author, Librarian, Book, Library
library_name = "Prince Albert Library"

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
author.book_set.all()

lib = Library.objects.get(name=library_name)
books = lib.books.all()

lib = Library.objects.get(name=library_name)
Librarian.objects.get(library=lib)
