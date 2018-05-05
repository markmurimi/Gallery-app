from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def images_of_day(request):
    date = dt.date.today() 
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def images_today(request):
    date = dt.date.today()
    return render(request, 'all-images/today-images.html', {"date": date,})

def past_days_images(request,past_date):
        # Converts data from the string Url
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(images_today)

    return render(request, 'all-images/past-images.html', {"date": date})

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Images for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)