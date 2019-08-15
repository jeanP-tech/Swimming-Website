from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import SaveForm
from django.shortcuts import redirect

import datetime

def index(request):
    return render(request, 'swimapp/index.html', {})

def save_date(request):
    form = SaveForm()
    return render(request, 'swimapp/pool.html', {'form': form})
