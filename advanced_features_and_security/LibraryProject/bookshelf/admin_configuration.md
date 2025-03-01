# Django Admin Configuration for the Book Model

## Steps to Configure the Admin Interface

1. **Register the `Book` Model:**
   - Open `bookshelf/admin.py`.
   - Import the `Book` model and register it with the admin:
     ```python
     from django.contrib import admin
     from bookshelf.models import Book

     admin.site.register(Book)
     ```

2. **Customize the Admin Interface:**
   - Create a custom admin class for the `Book` model:
     ```python
     class BookAdmin(admin.ModelAdmin):
         list_display = ('title', 'author', 'publication_year')
         list_filter = ('author', 'publication_year')
         search_fields = ('title', 'author')
     ```
   - Register the `Book` model with the custom admin class:
     ```python
     admin.site.register(Book, BookAdmin)
     ```

3. **Create a Superuser:**
   - Run the following command:
     ```bash
     python manage.py createsuperuser
     ```

4. **Access the Admin Interface:**
   - Start the development server:
     ```bash
     python manage.py runserver
     ```
   - Go to `http://127.0.0.1:8000/admin/` and log in.

5. **Verify the Customizations:**
   - Check that the `Book` list view displays `title`, `author`, and `publication_year`.
   - Ensure filters and search functionality are working