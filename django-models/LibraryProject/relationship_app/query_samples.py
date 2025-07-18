from django.db import models
from .models import Author, Librarian, Book

author = Author(name="Daniel")
author.save()
author.
