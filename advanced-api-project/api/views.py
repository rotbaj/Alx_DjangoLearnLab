from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticatedIsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List all books (Allow everyone to view)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view books

# Retrieve a single book by ID (Allow everyone to view)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view a single book

# Create a new book (Only authenticated users can create)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Ensure only logged-in users can create books

    def perform_create(self, serializer):
        """
        Save the book instance.
        Remove `user=self.request.user` unless Book has a user field.
        """
        serializer.save()

# Update an existing book (Only authenticated users can update)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Ensure only logged-in users can update books

    def perform_update(self, serializer):
        """
        Add custom logic before updating.
        If the Book model has an 'owner' field, check ownership here.
        """
        serializer.save()

# Delete a book (Only authenticated users can delete)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Ensure only logged-in users can delete books
