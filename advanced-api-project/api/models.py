from django.db import models

# Author model represents an author with a name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
# Book model represents a book with a title, publication year, and a foreign key to Author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

def __str__(self):
    return self.title
