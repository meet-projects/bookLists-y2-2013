# Create your views here.

from models import Book, Genre

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login




def home(request):
        return render(request, "books/homepage.html", {'user':request.user})

def get_Books(request,genre):
        fitGenre = Genre.objects.filter(name=str(genre))
        books = Book.objects.filter(genre=fitGenre)
        return render(request, "books/categorypage.html",
                      {'books': books, 'genre': fitGenre[0]})

        
           
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
        

        
