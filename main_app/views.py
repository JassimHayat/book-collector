from django.shortcuts import render # main_app/views.py
from django.http import HttpResponse
from .models import Book


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

# views.py

class Book  :
    def __init__(self, bookTitle, description, genre, releaseDate):
        self.bookTitle = bookTitle  
        self.description = description
        self.genre = genre
        self.releaseDate = releaseDate

# Create a list of Book instances
books = [
    Book('book1', 'description 1', 'horror', 2025),
    Book('book2', 'description 2', 'fantsy', 2002),
    Book('book3', 'description 3', 'fantsy', 2005),
]
