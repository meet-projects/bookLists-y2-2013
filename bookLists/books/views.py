# Create your views here.

from models import Book, Genre, Profile

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.models import User

def my_render(request, page, context):
	genres = Genre.objects.all()
	context['genres1'] = genres[:len(genres)/2]
	context['genres2'] = genres[len(genres)/2:]
	return render(request, page, context)

class UserRegistrationForm(forms.Form):
	 first_name = forms.CharField(label=u'first_name')
	 last_name = forms.CharField(label=u'last_name')
	 email = forms.CharField(label=u'Email')
	 password = forms.CharField(label=u'password',widget=forms.PasswordInput)
	 password_again = forms.CharField(label=u'password_again',widget=forms.PasswordInput)

class UploadImageForm(forms.Form):
    title = forms.CharField(max_length=50)##, label = u'Title')
    photo  = forms.ImageField()

def uploadPage(request):
        return my_render(request, 'books/uploadimage.html', {'form': UserImageForm()})

def upload(request):
        form = UploadImageForm(request.POST)
        if form.is_valid():
                photo = form.cleaned_data['photo']
                prof = Profile.objects.filter(user = request.user)[0]
                prof.photo = photo
                prof.save()
                return HttpResponseRedirect('get_profile')
        else:
                return HttpResponseRedirect('uploadPage')
                
                
def sign_up(request):
	return my_render(request, 'books/signup.html', {'form': UserRegistrationForm()})
def register(request):
	form = UserRegistrationForm(request.POST)
	if form.is_valid():
	#TODO Add functionality to save
		email = form.cleaned_data['email']
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
		password = form.cleaned_data['password']
		password_again = form.cleaned_data['password_again']
		if password != password_again:
			return my_render(request, 'books/signup.html', {'form': UserRegistrationForm(), 'message': 'passwords did not match' })
		elif len(User.objects.filter(username = email)):
			return my_render(request, 'books/signup.html', {'form': UserRegistrationForm(), 'message': 'ERROR: email already exists' })
		elif "" in [email, first_name, last_name, password, password_again]:
			return my_render(request, 'books/signup.html', {'form': UserRegistrationForm(), 'message': 'all fields should be filled' })
		else:
			user = User.objects.create_user(username = email, email=None, password=password, last_name=last_name, first_name=first_name)
			user.save()
			a = Profile(user = user, name = user.first_name + " " + user.last_name)
			a.save()
			user = authenticate(username=email, password =password)
			login(request, user)
			context = {'user': request.user}
	
			return my_render(request, 'books/homepage.html', context)

def home(request):
	return my_render(request, "books/homepage.html", {'user':request.user})

def get_genre(request,genre):
	fitGenre = Genre.objects.filter(name=str(genre))
	books = Book.objects.filter(genre=fitGenre)
	return my_render(request, "books/categorypage.html",
			  {'books': books, 'genre': fitGenre[0]})

def get_book(request, book):
	print book
	fitBook = Book.objects.filter(name =book)[0]
	print fitBook
	context = {'book':fitBook}
	
	return my_render(request, "books/bookpage.html", context)



def submitlogout(request):
	logout(request)
	return HttpResponseRedirect("home")

def market(request):
	 return my_render(request, "books/market.html", {})

def submitlogin(request):

	Email = request.POST['email']
	Password = request.POST['password']
	user = authenticate(username=Email, password=Password)
	login(request, user)
	context = {'user': request.user}
	return my_render(request, 'books/homepage.html', context)

def get_profile(request):
        return my_render(request, "books/profile.html", {'profile':Profile.objects.filter(user = request.user)[0]})
    
