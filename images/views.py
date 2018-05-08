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

def past_days_images(request):
        # Converts data from the string Url
    try:
        # date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        images = Post.objects.filter(pub_date__year='2011',pub_date__month='01',pub_date__day='01')
        return render(request, 'all-images/past-images.html', {'images':images})
    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_today)

    images = Post.days_images(date)
    return render(request, 'all-images/past-images.html', {"date": date, "images":images})

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

def image_details(request):
    return render(request,"all-images/imagedetails.html")