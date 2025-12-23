from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg
# Create your views here.

def index(request):
  books = Book.objects.all().order_by("title")
  num_books=books.count()
  avg_rating = books.aggregate(Avg("rating"))
  return render(request,'book_outlet/index.html',{
    "books":books,
    "total_num_of_books":num_books,
    "avg_rating":avg_rating 
  })

def book_details(request,slug):
  books = get_object_or_404(Book,slug=slug)
  return render(request,"book_outlet/book_details.html",{
    "title":books.title,
    "author":books.author,
    "rating":books.rating,
    "is_bestseller":books.is_bestseller
  })
