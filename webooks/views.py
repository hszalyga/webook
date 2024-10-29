from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound
# Create your views here.
def all_books(request):
    found_books = Book.find_all_books()
    context = {
        'books': found_books
    }
    return render(request, 'webooks/all_books.html', context)

def book_details(request, book_id):
    found_book = Book.find_all_books()
    for m in found_book:
        if m.book_id == book_id:
            context = {
                'book': m
            }
            return render(request,  'webooks/book_details.html', context)
    return HttpResponseNotFound('Film nie został znaleziony.')
