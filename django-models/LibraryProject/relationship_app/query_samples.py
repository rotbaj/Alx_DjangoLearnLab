import django
from django.core.exceptions import ObjectDoesNotExist
from relationship_app.models import Author, Book, Library, Librarian

# Setup Django
django.setup()

def get_books_by_author(author_name):
    """Query all books by a specific author."""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        if books.exists():
            print(f"Books by {author_name}: {[book.title for book in books]}")
        else:
            print(f"No books found for {author_name}.")
    except ObjectDoesNotExist:
        print(f"Author '{author_name}' not found.")

def get_books_in_library(library_name):
    """List all books in a library."""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        if books.exists():
            print(f"Books in {library_name}: {[book.title for book in books]}")
        else:
            print(f"No books found in {library_name}.")
    except ObjectDoesNotExist:
        print(f"Library '{library_name}' not found.")

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a specific library."""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Explicit usage of Librarian.objects.get(library=)
        print(f"The librarian for {library_name} is {librarian.name}.")
    except ObjectDoesNotExist:
        print(f"No librarian found for {library_name}.")

# Example Queries
if __name__ == "__main__":
    get_books_by_author("Chinua Achebe")
    get_books_in_library("National Library")
    get_librarian_for_library("National Library")
