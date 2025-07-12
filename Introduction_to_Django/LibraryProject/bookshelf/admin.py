from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these columns
    list_filter = ('author', 'publication_year')             # enable sidebar filters
    search_fields = ('title', 'author')                      # enable search bar

admin.site.register(Book, BookAdmin)
