import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

# Import models after Django setup
from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author '{author_name}' not found."

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian.name
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."
    except Librarian.DoesNotExist:
        return f"No librarian assigned to '{library_name}'."

# Sample Queries (for testing)
if __name__ == "__main__":
    print(books_by_author("Chinua Achebe"))
    print(books_in_library("National Library"))
    print(librarian_for_library("National Library"))
