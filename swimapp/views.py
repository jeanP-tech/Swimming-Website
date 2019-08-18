from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect, HttpResponseRedirect

import datetime

def index(request):
    form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

'''
def save():
    user_datetime = datetime.datetime.now()
    user_datetime.save()

def detail(request):

    #form = SaveForm()
    #return render(request, 'swimapp/pool.html', {'form': form})
'''
