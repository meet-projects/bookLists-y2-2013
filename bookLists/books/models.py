from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Genre(models.Model):
        name = models.CharField(max_length = 20)

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
        user = models.OneToOneField(User)
        booksLiked = models.ManyToManyField(Book)
        #photo = mo

class Rating(models.Model):
        book = models.ForeignKey("Book")
        profile = models.ForeignKey("Profile")
        date_added = models.DateTimeField(auto_now_add = True)
        rating = models.IntegerField()
        
        
