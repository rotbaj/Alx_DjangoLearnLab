## API Endpoints

### Books
- **List Books**: `GET /api/books/`
  - **Filtering**:
    - `title`: Filter by book title.
    - `author`: Filter by author.
    - `publication_year`: Filter by publication year.
  - **Searching**:
    - `search`: Search by title or author.
  - **Ordering**:
    - `ordering`: Order by `title` or `publication_year` (use `-` for descending order).
    
### Permissions
- **List and Retrieve**: Open to all users.
- **Create, Update, Delete**: Restricted to authenticated users.