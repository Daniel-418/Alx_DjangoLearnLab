from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class ListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self): #pyright: ignore
        return Book.objects.filter(owner=self.request.user)

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self): #pyright: ignore
        return Book.objects.filter(owner=self.request.user)

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #pyright: ignore
        return Book.objects.filter(owner=self.request.user)

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #pyright: ignore
        return Book.objects.filter(owner=self.request.user)

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #pyright: ignore
        return Book.objects.filter(owner=self.request.user)
