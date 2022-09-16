from django.urls import path


from .views import BookListViews

urlpatterns = [
    path("", BookListViews.as_view(), name="book_list"),

]