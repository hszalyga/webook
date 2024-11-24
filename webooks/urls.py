from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name='all_books_url'),
    path('add/', views.add_book, name='add_book_url'),
    path('<int:id>', views.book_details, name='book_details_url'),
    path('book_read', views.book_read, name='book_read_url'),
    path('collections/<int:id>', views.collection_details, name='collection_details_url'),
    path('about_me/', views.about_me, name='about_me_url')
    ]