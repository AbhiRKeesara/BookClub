from django.db import models

# Create your models here.


class Book(models.Model):
    book = models.CharField(max_length=100)
    description = models.TextField()
    read_by = models.DateField()
