from django.urls import path


from .views import BookListViews, BookDetailView


urlpatterns = [
    path("", BookListViews.as_view(), name="book_list"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_detail"),

]