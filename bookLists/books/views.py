# Create your views here.

from models import Book

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
        return HttpResponse("Congratz")

def get_Books(request,genre):

        books = Book.objects.filter(genre = genre)

        return HttpResponse("Genre Page")

        
        
        

        

        
