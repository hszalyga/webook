from django.shortcuts import render
from .models import Book
from django.http import HttpResponseNotFound
from django.db.models import Avg, Min, Max, Count
# Create your views here.
def all_books(request):
    title = request.GET.get('title')

    if title and len(title) > 3:
        found_books = Book.objects.filter(title__contains=title)
    else:
        found_books = Book.objects.all()

    found_books_aggregation = found_books.aggregate(Avg('statistics__average_rating'), Min('statistics__average_rating'),
                                                    Max('statistics__average_rating'), Count('id'))
    context = {
        'books': found_books,
        'aggregation_data': found_books_aggregation,
        'filter_title': title
    }
    return render(request, 'webooks/all_books.html', context)

def book_details(request, id):
    found_book = Book.objects.get(pk=id)
    if not found_book:
        return HttpResponseNotFound('Książka nie została znaleziona.')
    context = {
        'book': found_book
    }
    return render(request, 'webooks/book_details.html', context)

def add_book(request):
    return render(request, 'book/add_book.html')