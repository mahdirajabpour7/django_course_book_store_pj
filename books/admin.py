from django.contrib import admin
from .models import Book , Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user" , "book" , "text" , "datetime_create" ,)



admin.site.register(Book)
admin.site.register(Comment , CommentAdmin)

# Register your models here.
