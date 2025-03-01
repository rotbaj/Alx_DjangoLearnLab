# Permissions and Groups Setup

This Django application uses custom permissions and groups to restrict access to certain parts of the application.

## Permissions
The following custom permissions are defined in the `Book` model:
- `can_view_book`: Allows viewing books.
- `can_create_book`: Allows creating books.
- `can_edit_book`: Allows editing books.
- `can_delete_book`: Allows deleting books.

## Groups
The following groups are created and assigned permissions:
- **Viewers**: Can view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Views
Views are protected using Django's `permission_required` decorator:
- `book_list`: Requires `can_view_book`.
- `book_create`: Requires `can_create_book`.
- `book_edit`: Requires `can_edit_book`.
- `book_delete`: Requires `can_delete_book`.

## Testing
1. Create test users and assign them to groups.
2. Log in as each user and verify that permissions are enforced correctly.