from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.images_of_day,name='imagesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_images,name = 'pastImages')
]