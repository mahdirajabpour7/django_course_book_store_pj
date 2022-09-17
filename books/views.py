from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy



from .models import Book
#from .forms import NewPostFrom


class BookListViews(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "books/book_detail.html"


class BookCreateView(generic.CreateView):

    model = Book
    fields = ["title", "author", "text", "price"]
    template_name = "books/book_create.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ["title", "author", "text"]
    template_name = "books/book_update.html"



class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")



