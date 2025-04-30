from django.shortcuts import render, redirect # main_app/views.py
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required






class Home(LoginView):
    template_name = 'home.html'


class BookCreate(CreateView):
    model = Book
    fields = ['bookTitle','description', 'genre', 'releaseDate']
    # success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the book
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class BookUpdate(UpdateView):
    model = Book
    # Let's disallow the renaming of a book by excluding the name field!
    fields = ['description', 'genre', 'releaseDate']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'


# Define the home view function


def about(request):
    return render(request, 'about.html')

@login_required
def book_index(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'books/index.html', { 'books': books })

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})



def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('book-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    
