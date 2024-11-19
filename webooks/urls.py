from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books_url'),
    path('<id>', views.book_details, name='book_details_url'),
    path('add', views.add_book, name='add_book_url')
    ]