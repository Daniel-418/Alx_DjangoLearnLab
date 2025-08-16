from rest_framework import serializers
from datetime import date
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        year = attrs.get("publication_year")
        if year and year > date.today().year:
            raise serializers.ValidationError("Publication year cannnot be in the future")
        return attrs

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
