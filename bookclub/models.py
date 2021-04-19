from django.db import models

# Create your models here.
# Each model represents an entity inside your application - e.g. a book
# Each instance of your model represents a single row inside the database table.
# https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types


class Book(models.Model):
    book = models.CharField(max_length=100)
    description = models.TextField()
    read_by = models.DateField()


class Discussion(models.Model):
    book = models.ForeignKey("bookclub.Book",
                             related_name="discussion",
                             on_delete=models.CASCADE)
    author = models.ForeignKey("auth.User",
                               related_name="records",
                               on_delete=models.CASCADE)
    opinion = models.TextField()
