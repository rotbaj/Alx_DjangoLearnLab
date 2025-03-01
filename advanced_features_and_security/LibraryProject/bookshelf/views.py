from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Book
from .forms import BookForm
from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    search_query = request.GET.get('q', '').strip()
    books = Book.objects.all()

    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) | 
            Q(author__icontains=search_query)
        )  # Secure query to prevent SQL injection

    return render(request, 'bookshelf/book_list.html', {'books': books, 'search_query': search_query})

@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')
        else:
            messages.error(request, "There was an error in the form.")
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/book_form.html', {'form': form})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')
        else:
            messages.error(request, "Invalid data provided.")
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookshelf/book_form.html', {'form': form, 'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        try:
            book.delete()
            messages.success(request, "Book deleted successfully!")
            return redirect('book_list')
        except Exception as e:
            messages.error(request, "Error deleting book.")
            raise PermissionDenied("You do not have permission to delete this book.")

    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

# ✅ New Example View using ExampleForm
@login_required
def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle form data (e.g., save to DB, send an email, etc.)
            return redirect('book_list')  # Redirect after successful submission
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})