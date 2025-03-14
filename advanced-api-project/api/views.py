from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

# List all books (Allow everyone to view)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view books
    
    # Add filtering, searching, and ordering backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define fields that can be filtered
    filterset_fields = ['title', 'author', 'publication_year']

    # Define fields that can be searched (uses partial match by default)
    search_fields = ['title', 'author__name']

    # Define fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering by title

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
