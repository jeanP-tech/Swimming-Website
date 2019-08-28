from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import datetime, timedelta

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            
            obj = Userinfo()
            obj.user_city = form.cleaned_data['cities']
            obj.user_time = datetime.now()
            obj.user_timeinterval = form.cleaned_data['times']
            obj.save()

            '''
            user_city = form.cleaned_data['cities']
            user_time = datetime.now()
            user_timeinterval = form.cleaned_data['times']

            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().min)
            if hour >= 24:
                hour -= 24
                day = int(datetime.datetime.now().day + timedelta(days = 1))
                day.isoweekday()
            else:
            '''
            return HttpResponseRedirect('swimapp/pool')
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def instantview(request):
    return render(request, 'swimapp/pool.html', {})
