from django.db import models
from django.contrib import admin
from .models import Editor,Post,tags

admin.site.register(Editor)
admin.site.register(Post)
admin.site.register(tags)
# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save() 

class Meta:
    ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length =60)
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)