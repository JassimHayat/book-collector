from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    bookTitle = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    genre = models.CharField(max_length=100)
    releaseDate = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bookTitle

    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this books details
        return reverse('book-detail', kwargs={'book_id': self.id})