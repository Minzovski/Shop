from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", 'price')
    list_filter=('name',)
    list_editable=('price',)
    search_fields=('name', 'price')
