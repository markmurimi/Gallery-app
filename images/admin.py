from django.contrib import admin
from .models import Editor,Post, Location

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    admin.site.register(Editor)
    admin.site.register(Post)
    admin.site.register(Location)
