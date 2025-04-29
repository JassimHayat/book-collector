from django.shortcuts import render # main_app/views.py
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book



class BookCreate(CreateView):
    model = Book
    fields = ['bookTitle','description', 'genre', 'releaseDate']
    # success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    # Let's disallow the renaming of a book by excluding the name field!
    fields = ['description', 'genre', 'releaseDate']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'


# Define the home view function
def home(request):
    # Send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return render(request, 'about.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})
