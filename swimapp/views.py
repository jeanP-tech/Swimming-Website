from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import datetime, timedelta, time

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            user_city = form.cleaned_data['cities']
            user_time = datetime.now()
            user_timeinterval = int(form.cleaned_data['times'])
            day = datetime.now()

            hour = datetime.now().hour + user_timeinterval
            if hour >= 24:
                hour -= 24
                day = timedelta(days=1, hours=user_timeinterval) - timedelta(hours=24)
            weekday = day.isoweekday()
            pool_list = Timetable.objects.filter(day=weekday, start_time__gte=datetime.now(), end_time__lt=time(hour))
            return render(request, 'swimapp/pool.html', {'pool_list': pool_list})
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def instantview(request):
    return render(request, 'swimapp/pool.html', {})
