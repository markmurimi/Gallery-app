from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.images_today,name='imagesToday'),
    url(r'^post/(\d+)',views.post,name ='post'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_images,name = 'pastImages'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^details/', views.image_details, name='image_details')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
