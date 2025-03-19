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

## Comment System

The comment system allows users to interact with blog posts by adding, editing, and deleting comments.

### Features
- **Add Comment**: Authenticated users can add comments to blog posts.
- **Edit Comment**: Only the comment author can edit their comments.
- **Delete Comment**: Only the comment author can delete their comments.

### URLs
- **Add Comment**: `/posts/<int:post_id>/comments/new/`
- **Edit Comment**: `/comments/<int:pk>/edit/`
- **Delete Comment**: `/comments/<int:pk>/delete/`

### Permissions
- Only authenticated users can add comments.
- Only the comment author can edit or delete their comments.