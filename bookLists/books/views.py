# Create your views here.

from models import Book, Genre

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout




def home(request):
        return render(request, "books/homepage.html", {'user':request.user})

def get_genre(request,genre):
        fitGenre = Genre.objects.filter(name=str(genre))
        books = Book.objects.filter(genre=fitGenre)
        return render(request, "books/categorypage.html",
                      {'books': books, 'genre': fitGenre[0]})

def get_book(request, book):
        fitBook = Book.objects.filter(name =str(book))
        context = {'book':fitBook}
        
	return render(request, "books/bookpage.html", context)

def logout_user(request):

 logout(request)
 return HttpResponseRedirect("home")

def market(request):
	 return render(request, "books/market.html", {})

        
           
def submitlogin(request):

    Email = request.POST['email']
    Password = request.POST['password']
    user = authenticate(username=Email, password=Password)
    context = {'user': request.user}
    if user is not None:
        print "Cleared for takeoff"
    else:

        print "Invalid log in attempt"
            

    
    return render(request, 'books/homepage.html', context)
        

        
