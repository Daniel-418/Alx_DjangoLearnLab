from rest_framework.generics import ListAPIView
from .models import Book

class BookSerializer(ListAPIView):
    class Meta:
        model = Book
        fields = ['title', 'author']
