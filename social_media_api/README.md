# API Documentation (README.md)

## Follow and Unfollow Users

### Follow a User
**Endpoint:** `POST /api/accounts/follow/{user_id}/`

**Response:**
```json
{
  "status": "following"
}
```

### Unfollow a User
**Endpoint:** `POST /api/accounts/unfollow/{user_id}/`

**Response:**
```json
{
  "status": "unfollowed"
}
```

## Get User Feed

### Retrieve Posts from Followed Users
**Endpoint:** `GET /api/posts/feed/`

**Response:**
```json
[
  {
    "id": 1,
    "author": "user123",
    "title": "Post Title",
    "content": "Post content here...",
    "created_at": "2025-03-29T12:00:00Z",
    "updated_at": "2025-03-29T12:00:00Z"
  }
]
```
