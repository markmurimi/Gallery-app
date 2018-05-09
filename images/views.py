from django.shortcuts import render,redirect, get_object_or_404
import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Post
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def images_today(request):
    date = dt.date.today()
    images = Post.todays_images()
    return render(request, 'all-images/today-images.html', {"date": date,"images":images})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})
    
def post(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/post.html", {"post":post})

def all_images(request):
    images = Post.all_images()
    return render(request, 'all_images.html', {"images":images})


def image_details(request, post_id):
    photo = Post.objects.get(id=post_id)
    return render(request,"all-images/imagedetails.html",{'photo':photo})