from django.shortcuts import render, redirect
from .forms import BookForm, ReviewForm
from .models import Book, Review

# Create your views here.

def book_list(request):
    context = {'book_list':Book.objects.all()}
    return render(request,"book_register/book_list.html", context)

def book_form(request, id=0):
    if request.method =='GET':
        if id==0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request,"book_register/book_form.html", {'form':form})
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('/book/list')

def book_delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('/book/list')

def review_form(request):
    if request.method == "GET":
        form_review = ReviewForm()
        return render(request,"book_register/review_form.html", {'form_review':form_review})
    else:
        form_review = ReviewForm(request.POST)
        if form_review.is_valid():
            form_review.save()
        return redirect('/book/review-list')

def review_list(request):
    context_review = {'review_list':Review.objects.all()}
    return render(request,"book_register/review_list.html", context_review)
