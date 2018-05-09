from django.db import models
import datetime as dt
# Create your models here.

class Location(models.Model):
    """ class to indicate where the image was taken"""
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save() 

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length =60)
    editor = models.ForeignKey(Editor)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')
    descripton = models.TextField()
    image_id = models.CharField(max_length = 30)
    location_taken = models.ForeignKey(Location)
    
    def __str__(self):
        return self.title

    @classmethod
    def all_images(cls):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date = today)
        return images

    @classmethod
    def days_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images

