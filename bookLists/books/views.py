# Create your views here.

from models import Book, Genre

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
        return render(request, "books/homepage.html", {})

def get_Books(request,genre):
        genre = Genre.objects.filter(name=str(genre))
        books = Book.objects.filter(genre=genre[0])
        return render(request, "books/categorypage.html",
                      {'books': books, 'genre': genre[0]})

        
        
        

        

        
