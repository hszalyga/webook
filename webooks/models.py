from django.db import models
import csv
import datetime

# Create your models here.
class Book:
    def __init__(self, book_id, title, authors, original_publication_year, average_rating, rating_count, image_url):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.original_publication_year = original_publication_year
        self.average_rating = average_rating
        self.rating_count = rating_count
        self.image_url = image_url

    @staticmethod
    def find_all_books():
        books_list = []

        with open('webooks/migrations/books.csv', 'r', encoding='utf8') as all_books_file:
            reader = csv.DictReader(all_books_file, delimiter=',')

            for row in reader:
                books_list.append(Book(
                    row['book_id'],
                    row['title'],
                    row['authors'],
                    row['original_publication_year'],
                    float(row['average_rating']),
                    int(row.get('ratings_count', 0)),
                    row['image_url'],
                ))

        return books_list