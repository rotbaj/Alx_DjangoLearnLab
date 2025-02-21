from django.urls import path
from .views import list_books, LibraryDetailView, register, user_login, user_logout

urlpatterns = [
    path("books/", list_books, name="list_books"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
]
