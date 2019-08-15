from django.shortcuts import render
from .models import City, Pool, Price, Timetable
from django.http import Http404
from .forms import SaveForm

import datetime

def index(request):
    return render(request, 'swimapp/index.html', {})

def save_date(request):
    form = SaveForm()
    return render(request, 'swimapp/pool_page.html', {'form': form})
