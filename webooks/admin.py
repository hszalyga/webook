from django.contrib import admin
from webooks.models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('statistics__average_rating', 'title', 'authors')
    list_display = (
        'book_id', 'title', 'authors', 'language_code', 'original_publication_year',
        'average_rating', 'ratings_count', 'small_image_url', 'image_url'
    )

    def average_rating(self, obj):
        return obj.statistics.average_rating
    def ratings_count(self, obj):
        return obj.statistics.ratings_count

# Register your models here.
admin.site.register(Book, BookAdmin)