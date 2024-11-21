from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class BookStatistics(models.Model):
    average_rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    ratings_count = models.IntegerField(validators=[MinValueValidator(0)])

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(validators=[MinValueValidator(1)])
    title = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    language_code = models.CharField(max_length=10)
    original_publication_year = models.IntegerField(validators=[MaxValueValidator(4)])
    statistics = models.OneToOneField(BookStatistics, on_delete=models.CASCADE)
    small_image_url = models.URLField()
    image_url = models.URLField()

    def __str__(self):
        return self.title

class BookRead(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)