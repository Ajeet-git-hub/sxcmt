from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from library.models import *
from django.contrib.auth import authenticate, login
from .forms import Work_form
# Create your views here.

def Front_look(request):
    book = Book.objects.order_by("-book_title")[:5]
    try:
        book = Book.objects.filter(book_title__contains = request.POST["find"])
        category = request.POST['options']
        if(category == "Title"):
            book = Book.objects.filter(book_title__contains = request.POST["find"])
        elif(category == "Publisher"):
            book = Book.objects.filter(book_publisher__contains = request.POST["find"])
        elif(category == "Author"):
            book = Book.objects.filter(book_author__contains = request.POST["find"])
    except:
        book = Book.objects.order_by("-book_title")[:5]
    return render(request, "library/front.html",{"book":book})

stu_roll = None 
def Avalability(request):
        try:
            global stu_roll
            stu_roll = request.POST["stu_roll"]
            try:
                st_r = Student.objects.get(student_roll = stu_roll)                
                total_books = st_r.book.count()                
                book_list = st_r.book.filter(book_title__startswith = "")                
                return render(request, "library/work.html",
                {"report":"Done!", "total_books":total_books, "roll":stu_roll, "book_li":book_list})
            except:
                return render(request, "library/work.html", {"report":"Wrong Roll No!!"})
        except:
            return render(request, "library/work.html", {"report":"Error Lol"})
    
def Work_area(request):
    try:
        global stu_roll
        book_id = request.POST["bk_id"]
        try:
            st_r = Student.objects.get(student_roll = stu_roll)
        except:
            return render(request, "library/work.html", {"report":"Wrong Roll No!"})
        try:
            bk_i = Book.objects.get(book_code = book_id)
        except:
            return render(request, "library/work.html", {"report":"Wrong Book Code","roll":stu_roll})
        try:
            try:
                st_r.objects.get(book = bk_i)
                return render(request, "library/work.html", {"report":"Already exist"})
            except:
                st_r.book.add(bk_i)
                bk_i.book_left -= 1   
                bk_i.save()
                return render(request, "library/work.html", {"report":"Done", "stu_roll":stu_roll, "bk_left":bk_i})
        except:
            return render(request, "library/work.html", {"report":"Not Able to add"})
    except:
        return render(request, "library/work.html", {"report":"Enter the values"})
        
