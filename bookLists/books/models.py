from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Genre(models.Model):
        name = models.CharField(max_length = 20)

        background_image = models.CharField(max_length = 30) 
        def __unicode__(self):
                return self.name

        ##bgImage = models.ImageField(

        
class Book(models.Model):
        name = models.CharField(max_length = 40)
        author = models.CharField(max_length = 30)
        genre = models.ForeignKey("Genre")
        summary = models.CharField(max_length = 1000)
        year = models.CharField(max_length = 4)
        cover = models.CharField(max_length = 30)

        def __unicode__(self):
                return self.name
        
        ## image

class Profile(models.Model):
	#def get_code:
        user = models.OneToOneField(User)
	email = models.CharField(max_length = 200)
        name = models.CharField(max_length = 40)
##        booksLiked = models.ManyToManyField(Book)
##        photo = models.ImageField(upload_to = "books/static/images")

class Rating(models.Model):
        book = models.ForeignKey("Book")
        profile = models.ForeignKey("Profile")
        date_added = models.DateTimeField(auto_now_add = True)
        rating = models.IntegerField()
 
class Comment(models.Model):
	profile = models.ForeignKey('Profile')
	comment = models.CharField(max_length = 1000)
        
