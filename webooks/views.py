from django.shortcuts import render
from .models import Book

# Create your views here.
def all_books(request):
    found_books = Book.find_all_books()
    context = {
        'books': found_books
    }
    return render(request, 'book/all_books.html', context)