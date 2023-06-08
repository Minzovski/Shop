from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class BookList(ListView):
    model = Book
    context_object_name = 'book'
    template_name='book.html'
# Create your views here.
