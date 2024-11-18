from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(validators=[MinValueValidator(1)])
    title = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    language_code = models.CharField(max_length=10)
    original_publication_year = models.IntegerField(default=0, validators=[MaxValueValidator(4)])
    average_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ratings_count = models.IntegerField(validators=[MinValueValidator(0)])
    small_image_url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

    # def __init__(self, book_id, title, authors, language, original_publication_year, average_rating, rating_count, small_image_url):
    #     self.book_id = book_id
    #     self.title = title
    #     self.authors = authors
    #     self.language = language
    #     self.original_publication_year = original_publication_year
    #     self.average_rating = average_rating
    #     self.rating_count = rating_count
    #     self.image_url = small_image_url

    # @staticmethod
    # def find_all_books():
    #     books_list = []
    #
    #     with open('webooks/migrations/books.csv', 'r', encoding='utf8') as all_books_file:
    #         reader = csv.DictReader(all_books_file, delimiter=',')
    #
    #         for row in reader:
    #             books_list.append(Book(
    #                 book_id=row['book_id'],
    #                 title=row['title'],
    #                 authors=row['authors'],
    #                 language_code=row['language_code'],
    #                 original_publication_year=row['original_publication_year'],
    #                 average_rating=float(row['average_ratings']),
    #                 ratings_count=int(row.get('ratings_count', 0)),
    #                 small_image_url=row['small_image_url'],
    #                 image_url=row['image_url'],
    #             ))
    #
    #     return books_list
    #
