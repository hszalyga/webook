# Generated by Django 5.0.9 on 2024-11-24 12:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webooks', '0004_alter_book_original_publication_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='original_publication_year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]