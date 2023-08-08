from django.db import models
from django.utils import timezone
# Create your models here.

"""class Quantity(models.Model):
    number = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return str(self.number)"""

class Book(models.Model):
    #book_quantity = models.ForeignKey(Quantity, on_delete = models.CASCADE)
    book_title = models.CharField(max_length = 100)
    book_author = models.CharField(max_length = 100)
    book_publisher = models.CharField(max_length = 100)
    book_code = models.CharField(max_length = 15, unique = True)
    book_total = models.PositiveIntegerField(default = 0)    
    book_left = models.PositiveIntegerField(default = 0)
    def __str__(self):
        return self.book_title

class Student(models.Model):
    book = models.ManyToManyField(Book, blank = True)
    student_name = models.CharField(max_length = 40)
    student_roll = models.CharField(max_length = 20, unique = True)
    def __str__ (self):
        return self.student_name        
    