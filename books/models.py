from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="cover/", blank=True)
    #1299.57


    def __str__(self):
        return f"{self.title}:{self.author}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])


class Comment(models.Model):
    text = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE , related_name="comments")

    def __str__(self):
        return f'{self.user}: {self.text}'