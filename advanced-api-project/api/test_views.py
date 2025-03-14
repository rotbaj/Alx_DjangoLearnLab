from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client = APIClient()

        # Create a test book
        self.book = Book.objects.create(
            title='1984',
            author='George Orwell',
            publication_year=1949
        )

    def test_create_book(self):
        """
        Ensure we can create a new book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-create')
        data = {
            'title': 'Animal Farm',
            'author': 'George Orwell',
            'publication_year': 1945
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # Check that the book was created

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a book.
        """
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_update_book(self):
        """
        Ensure we can update a book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': '1984',
            'author': 'George Orwell',
            'publication_year': 1948  # Update the publication year
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['publication_year'], 1948)

    def test_delete_book(self):
        """
        Ensure we can delete a book.
        """
        self.client.force_authenticate(user=self.user)  # Authenticate the user
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Check that the book was deleted

    def test_filter_books(self):
        """
        Ensure we can filter books by title, author, and publication_year.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the filter

    def test_search_books(self):
        """
        Ensure we can search books by title and author.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Orwell'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book matches the search

    def test_order_books(self):
        """
        Ensure we can order books by title and publication_year.
        """
        # Create a second book for ordering tests
        Book.objects.create(
            title='Animal Farm',
            author='George Orwell',
            publication_year=1945
        )
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], '1984')  # First book in ascending order

    def test_unauthenticated_access(self):
        """
        Ensure unauthenticated users cannot create, update, or delete books.
        """
        url_create = reverse('book-create')
        url_update = reverse('book-update', args=[self.book.id])
        url_delete = reverse('book-delete', args=[self.book.id])

        # Test create
        response = self.client.post(url_create, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test update
        response = self.client.put(url_update, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test delete
        response = self.client.delete(url_delete)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)