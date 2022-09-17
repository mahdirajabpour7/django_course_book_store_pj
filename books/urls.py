from django.urls import path


from .views import BookListViews, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path("", BookListViews.as_view(), name="book_list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("new/", BookCreateView.as_view(), name="book_create"),
    path("<int:pk>/edit/", BookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),

]