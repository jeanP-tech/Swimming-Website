from django.shortcuts import render
from .models import City, Pool, Price, Timetable
from django.http import HttpResponse
import datetime

'''
def index(request):
    return render(request, 'swimapp/index.html', {})
'''

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
