# Create your views here.

from models import Book, Genre

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login




def home(request):
        return render(request, "books/homepage.html", {'user':request.user})

def get_genre(request,genre):
        fitGenre = Genre.objects.filter(name=str(genre))
        books = Book.objects.filter(genre=fitGenre)
        return render(request, "books/categorypage.html",
                      {'books': books, 'genre': fitGenre[0]})

def get_book(request, book):
        print book
        fitBook = Book.objects.filter(name =book)[0]
        print fitBook
        context = {'book':fitBook}
        
	return render(request, "books/bookpage.html", context)



def market(request):
	 return render(request, "books/market.html", {})

        
           
def submitlogin(request):

    Email = request.POST['email']
    Password = request.POST['password']
    user = authenticate(username=Email, password=Password)
    login(request, user)
    context = {'user': request.user}
    return render(request, 'books/homepage.html', context)        
