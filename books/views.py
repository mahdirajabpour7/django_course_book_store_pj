from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from .models import Book
#from .forms import NewPostFrom


class BookListViews(generic.ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"


#class BookDetailView(generic.DetailView):
    #model = Book
    #template_name = "books/book_detail.html"
def book_detail_view(request , pk):
    book=get_object_or_404(Book , pk=pk)
    book_comment=book.comments.all()
    return render(request, "books/book_detail.html",{"book":book , "comments":book_comment})


class BookCreateView(generic.CreateView):

    model = Book
    fields = ["title", "author", "text", "price", "cover",]
    template_name = "books/book_create.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ["title", "author", "text", "cover",]
    template_name = "books/book_update.html"



class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("book_list")



