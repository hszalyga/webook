from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound
from django.db.models import Avg, Min, Max, Count
# Create your views here.
def all_books(request):
    found_books = Book.objects.all() #pobieranie filmów z bazy danych
    found_books_aggregation = found_books.aggregate(Avg('average_rating'), Min('average_rating'),
                                                    Max('average_rating'), Count('id'))

    context = {
        'books': found_books,
        'aggregation_data': found_books_aggregation
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