from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.images_of_day,name='imagesToday')
]