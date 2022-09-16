from django.shortcuts import render
from django.views import generic



from .models import Book


class BookListViews(generic.ListView):
    model = Book
    template = "books/book_list.html"
    context_object_name = "books"

