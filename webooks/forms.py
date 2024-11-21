from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class BookForm(forms.Form):
    book_id = forms.IntegerField(validators=[MinValueValidator(1)])
    title = forms.CharField(label='Book title', max_length=1000)
    authors = forms.CharField(label='Book authors',max_length=1000)
    language_code = forms.CharField(label='Book language',max_length=10)
    original_publication_year = forms.IntegerField(label='Book publication year',initial=0, validators=[MaxValueValidator(4)])
    # average_rating = forms.FloatField(label='Book average rating',validators=[MinValueValidator(0), MaxValueValidator(10)])
    # ratings_count = forms.IntegerField(label='Book ratings count',validators=[MinValueValidator(0)])
    small_image_url = forms.URLField(label='Book cover small image URL')
    image_url = forms.URLField(label='Book cover image URL')

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'uk-input uk-margin-small-bottom'