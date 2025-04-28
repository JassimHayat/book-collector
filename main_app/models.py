from django.db import models

class Book(models.Model):
    bookTitle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    genre = models.TextField(max_length=250)
    releaseDate = models.IntegerField()

def __str__(self):
        return self.bookTitle