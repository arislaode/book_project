from django.db import models

# Create your models here.

class BookList(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Book(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=14)
    book = models.ForeignKey(BookList, on_delete=models.CASCADE)
    start_date = models.DateField("Start Date(mm/dd/2020)", auto_now_add=False, auto_now=False, blank=True, null=True)
    end_date = models.DateField("Start Date(mm/dd/2020)", auto_now_add=False, auto_now=False, blank=True, null=True)

class Review(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    book = models.ForeignKey(BookList, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
