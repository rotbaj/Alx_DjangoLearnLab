from rest_framework import serializers
from .models import Author, Book
import datetime

# BookSerializer serializes all fields of the Book model and includes custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value 
    
    class Meta:
        model = Book
        fields = '__all__'

# AuthorSerializer serializes the Author model and includes a nested BookSerializer to handle related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']