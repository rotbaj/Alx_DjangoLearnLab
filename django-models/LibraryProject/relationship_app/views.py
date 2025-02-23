from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book  
from .models import Library
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  

def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def library_detail(request, library_id):
    """Function-based view to display details of a library."""
    library = Library.objects.get(id=library_id)
    return render(request, "relationship_app/library_detail.html", {"library": library})  

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def register(request):
    """Handles user registration"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the new user automatically
            return redirect("list_books")  # Redirect after successful registration
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def user_login(request):
    """Handles user login"""
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {"form": form})

def user_logout(request):
    """Handles user logout"""
    logout(request)
    return redirect("login")  # Redirect to login page after logout

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin View
@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian View
@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# Member View
@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, "relationship_app/member_view.html")