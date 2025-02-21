# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    def get_queryset(self):
         return Library.objects.all()  # Important: Specify queryset