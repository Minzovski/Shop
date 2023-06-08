# Generated by Django 4.2.1 on 2023-05-30 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(default=None, max_length=50),
        ),
    ]