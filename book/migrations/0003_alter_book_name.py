# Generated by Django 4.2.1 on 2023-05-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_description_book_pages_book_price_book_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
