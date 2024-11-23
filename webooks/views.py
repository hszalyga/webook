from django.shortcuts import render, redirect
from .models import Book, BookStatistics, BookRead
from django.http import HttpResponseNotFound
from django.db.models import Avg, Min, Max, Count
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
@login_required
def all_books(request):
    title = request.GET.get('title')

    if title and len(title) > 3:
        found_books = Book.objects.filter(title__contains=title)
    else:
        found_books = Book.objects.all()[:1000]

    found_books_aggregation = found_books.aggregate(Avg('statistics__average_rating'), Min('statistics__average_rating'),
                                                    Max('statistics__average_rating'), Count('id'))
    context = {
        'books': found_books,
        'aggregation_data': found_books_aggregation,
        'filter_title': title
    }
    return render(request, 'webooks/all_books.html', context)

@login_required
def book_details(request, id):
    found_book = Book.objects.get(pk=id)
    if not found_book:
        return HttpResponseNotFound('Książka nie została znaleziona.')
    context = {
        'book': found_book
    }
    return render(request, 'webooks/book_details.html', context)

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            #tutaj jest zapis do bazy danych:
            book_data = form.cleaned_data
            stats = BookStatistics.objects.create(average_rating=0, ratings_count=0)
            Book.objects.create(
                book_id=book_data['book_id'],
                title=book_data['title'],
                authors=book_data['authors'],
                language_code=book_data['language_code'],
                original_publication_year=book_data['original_publication_year'],
                small_image_url =book_data['small_image_url'],
                image_url =book_data['image_url'],
                statistics=stats
            )
        return redirect('all_books_url')
    form = BookForm()
    context = {
        'book_form': form
    }
    return render(request, 'webooks/add_book.html', context)

@login_required
def book_read(request):
    logged_user = request.user

    if request.method == 'POST':
        name = request.POST['collection_name']
        BookRead.objects.create(name=name, owner=logged_user)
        return redirect('book_read_url')

    book_reads = BookRead.objects.filter(owner=logged_user).annotate(book_count=Count('books'))
    context = {
        'collections': book_reads
    }
    return render(request, 'webooks/book_read.html', context)