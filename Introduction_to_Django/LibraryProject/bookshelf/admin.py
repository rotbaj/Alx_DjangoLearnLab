from django.contrib import admin
from bookshelf.models import Book

# Custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters for the list view
    list_filter = ('author', 'publication_year')

    # Enable search functionality
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)