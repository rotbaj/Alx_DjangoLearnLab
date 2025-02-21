```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by attempting to retrieve the book
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book does not exist.")

Book does not exist.
