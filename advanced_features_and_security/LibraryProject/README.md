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

# Security Measures Implemented

## 1. Django Security Settings
- `DEBUG = False` to prevent detailed error messages.
- `ALLOWED_HOSTS` restricts access to known domains.
- `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF` prevent XSS and Clickjacking.
- `CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE` ensure secure cookies over HTTPS.

## 2. CSRF Protection
- All forms include `{% csrf_token %}`.
- `CSRF_COOKIE_SECURE = True` ensures CSRF protection is enforced over HTTPS.

## 3. SQL Injection Prevention
- Views use Django ORM instead of raw SQL.
- `Q()` object ensures safe query handling.

## 4. Content Security Policy (CSP)
- Uses `django-csp` to limit script and style sources.
- Blocks inline scripts except explicitly allowed sources.

## 5. Testing and Validation
- **Manual testing**: Check forms for XSS/SQL injection vulnerabilities.
- **Automated security testing**: Use `django-debug-toolbar` and `OWASP ZAP`.
