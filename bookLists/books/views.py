# Create your views here.

from models import Book, Genre

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
        return render(request, "books/homepage.html", {})

def get_Books(request,genre):
        fitGenre = Genre.objects.filter(name=str(genre))
        books = Book.objects.filter(genre=fitGenre)
        return render(request, "books/categorypage.html",
                      {'books': books, 'genre': fitGenre[0]})

        
        
        

        

        
