from django.db import models
import csv
import datetime

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length =255)
    title = models.CharField(max_length =1000)
    authors = models.CharField(max_length =1000)
    language = models.CharField(max_length =10)
    original_publication_year = models.DateField()
    average_rating = models.DecimalField(max_digits =5, decimal_places=2)
    rating_count = models.IntegerField()
    small_image_url = models.TextField()

    # def __init__(self, book_id, title, authors, language, original_publication_year, average_rating, rating_count, small_image_url):
    #     self.book_id = book_id
    #     self.title = title
    #     self.authors = authors
    #     self.language = language
    #     self.original_publication_year = original_publication_year
    #     self.average_rating = average_rating
    #     self.rating_count = rating_count
    #     self.image_url = small_image_url

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
                    row['language_code'],
                    row['original_publication_year'],
                    float(row['average_rating']),
                    int(row.get('ratings_count', 0)),
                    row['small_image_url'],
                ))

        return books_list

