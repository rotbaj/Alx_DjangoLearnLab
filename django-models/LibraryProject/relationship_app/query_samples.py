import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    # Create an author
    author, _ = Author.objects.get_or_create(name="Chinua Achebe")

    # Create a book
    book, _ = Book.objects.get_or_create(title="Things Fall Apart", author=author)

    # Create a library
    library, _ = Library.objects.get_or_create(name="National Library")
    library.books.add(book)

    # Create a librarian
    librarian, _ = Librarian.objects.get_or_create(name="John Doe", library=library)

def query_books_by_author(author_name):
    author = Author.objects.filter(name=author_name).first()
    if author:
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}: {[book.title for book in books]}")
    else:
        print(f"Author '{author_name}' not found.")

def list_books_in_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        books = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books]}")
    else:
        print(f"Library '{library_name}' not found.")

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Using get() instead of filter().first()
        print(f"Librarian for {library_name}: {library.librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")

def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Using get() to fetch a single author
        books = Book.objects.filter(author=author)
        if books.exists():
            print(f"Books by {author_name}: {[book.title for book in books]}")
        else:
            print(f"No books found for {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")

# Example usage:
get_books_by_author("Chinua Achebe")

if __name__ == "__main__":
    create_sample_data()
    query_books_by_author("Chinua Achebe")
    list_books_in_library("National Library")
    retrieve_librarian_for_library("National Library")
