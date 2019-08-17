from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import SaveForm
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.core.urlresolvers import reverse

import datetime

def index(request):
    return render(request, 'swimapp/index.html', {})

def save():
    user_datetime = datetime.datetime.now()
    user_datetime.save()

def detail(request):

    #form = SaveForm()
    #return render(request, 'swimapp/pool.html', {'form': form})
