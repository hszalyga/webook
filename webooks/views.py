from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound
# Create your views here.
def all_books(request):
    found_books = Book.objects.all() #pobieranie filmów z bazy danych
    context = {
        'books': found_books
    }
    return render(request, 'webooks/all_books.html', context)

def book_details(request, id):
    found_book = Book.object.get(pk=id)
    if not found_book:
        return HttpResponseNotFound('Książka nie została znaleziona.')
    context = {
        'book': found_book
    }
    return render(request, 'webooks/book_details.html', context)