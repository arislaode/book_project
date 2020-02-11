from django.db import models

# Create your models here.

class BookOrder(models.Model):
    name = models.CharField(max_length=60)
    name_book = models.CharField(max_length=60)
    contact = models.CharField(max_length=14)
    address = models.CharField(max_length=200)