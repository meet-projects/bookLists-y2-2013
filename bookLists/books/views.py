# Create your views here.

from models import Book

from django.http import HttpResponse

def home(request):

        

        return HttpResponse("Congratz")

def get_Books(request,genre):

        books = Book.objects.filter(genre = genre)

        return HttpResponse("Genre Page")

        
        
        

        

        
