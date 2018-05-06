from django.contrib import admin
from .models import Editor,Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    admin.site.register(Editor)
    admin.site.register(Post)

