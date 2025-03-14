from django.urls import path
from .views import (
    BookListView,       # List all books
    BookDetailView,     # Retrieve a single book by ID
    BookCreateView,     # Create a new book
    BookUpdateView,     # Update an existing book
    BookDeleteView      # Delete a book
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update an existing book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]