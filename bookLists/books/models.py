from django.db import models



# Create your models here.



class Genre(models.Model):
        
        name = models.CharField(max_length = 20)

        background_image = models.CharField(max_length = 30)

        def __unicode__(self):
                return self.name

        

        
class Book(models.Model):
        name = models.CharField(max_length = 40)
        author = models.CharField(max_length = 30)
        genre = models.ForeignKey("Genre")
        summary = models.CharField(max_length = 1000)
        year = models.CharField(max_length = 4)
        cover = models.CharField(max_length = 30)

        def __unicode__(self):
                return self.name

class Profile(models.Model):
        pass
