# Generated by Django 5.0.9 on 2024-11-20 17:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webooks', '0003_bookread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='original_publication_year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(4)]),
        ),
    ]