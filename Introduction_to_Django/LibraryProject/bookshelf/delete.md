# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

(1, {'bookshelf.Book': 1})

try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book does not exist.")

Book does not exist.