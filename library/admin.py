from django.contrib import admin
from library.models import Book, Student#, Quantity

# Register your models here.
admin.site.register(Book)
admin.site.register(Student)
#admin.site.register(Quantity)
