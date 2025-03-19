## Blog Post Management

The blog post management system supports **CRUD (Create, Read, Update, Delete)** operations for authenticated users.

### Features
- **Create Post**: Authenticated users can create new posts.
- **Read Post**: All users can view the list of posts and individual post details.
- **Update Post**: Only the author of a post can edit it.
- **Delete Post**: Only the author of a post can delete it.

### URLs
- **List Posts**: `/posts/`
- **Create Post**: `/post/new/`
- **View Post**: `/post/<int:pk>/`
- **Edit Post**: `/post/<int:pk>/update/`
- **Delete Post**: `/post/<int:pk>/delete/`

### Permissions
- Only authenticated users can create posts.
- Only the author of a post can edit or delete it.
- All users can view posts.