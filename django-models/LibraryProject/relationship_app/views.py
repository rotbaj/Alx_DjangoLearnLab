from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book  
from .models import Library  

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def library_detail(request, library_id):
    """Function-based view to display details of a library."""
    library = Library.objects.get(id=library_id)
    return render(request, "relationship_app/library_detail.html", {"library": library})  
