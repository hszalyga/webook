from django.db import migrations
from webooks.models import Book
from django.db import transaction

import datetime
import csv


def load_initial_data(apps, schema_editor):
    books_list = []

    with open('webooks/migrations/books.csv', 'r', encoding='utf8') as all_books_file:
        reader = csv.DictReader(all_books_file, delimiter=',')

        for row in reader:
            books_list.append(Book(
                book_id=row['book_id'],
                title=row['title'],
                authors=row['authors'],
                language_code=row['language_code'],
                original_publication_year=row['original_publication_year'],
                average_rating=row['average_rating'],
                ratings_count=row['ratings_count'],
                small_image_url=row['small_image_url'],
                image_url=row['image_url'],
            ))

    Book.objects.bulk_create(books_list)


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('webooks', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
