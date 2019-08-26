from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import datetime, timedelta

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            '''
            obj = Userinfo()
            obj.user_city = form.cleaned_data['cities']
            obj.user_time = datetime.now()
            obj.user_timeinterval = form.cleaned_data['times']
            obj.save()
            '''
            user_city = form.cleaned_data['cities']
            user_time = datetime.now()
            user_timeinterval = form.cleaned_data['times']

            day_now = int(datetime.datetime.now().day)
            hour_now = int(datetime.datetime.now().hour)
            if hour_now >= 24:
                hour_now -= 24
                day_now += timedelta(days = 1)

            min_now = int(datetime.datetime.now().min)
            return HttpResponseRedirect('swimapp/pool')
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def instantview(request):
    return render(request, 'swimapp/pool.html', {})
