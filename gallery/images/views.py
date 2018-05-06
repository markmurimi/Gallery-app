from django.shortcuts import render,redirect
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

def past_days_images(request,past_date):
        # Converts data from the string Url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_today)
        
    images = Post.days_images(date)
    return render(request, 'all-images/past-images.html', {"date": date, "images":images})
    
    