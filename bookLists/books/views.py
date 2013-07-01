# Create your views here.

from models import Book

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
        return render(request, "books/homepage.html", {})

def get_Books(request,genre):

        books = Book.objects.filter(genre = genre)

        Genre = genre

        return HttpResponse("Genre Page")

        
        
        

        

        
