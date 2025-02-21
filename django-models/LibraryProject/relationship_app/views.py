from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library 
from .models import Book 

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def library_detail(request, library_id):
    library = Library.objects.get(id=library_id)
    return render(request, 'library_detail.html', {'library': library})
