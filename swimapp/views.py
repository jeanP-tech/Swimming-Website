from django.shortcuts import render
from .models import City, Pool, Price, Timetable, TimeInterval
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import date, datetime, timedelta, time

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            user_city = form.cleaned_data['cities']
            user_time = datetime.now()
            user_timeinterval = int(form.cleaned_data['times'])
            date = datetime.now()
            '''
            time = datetime.now().hour + user_timeinterval
            if hour >= 24:
                hour -= 24
                date = timedelta(days=1, hours=user_timeinterval) - timedelta(hours=24)
            '''
            transfered_date = date + timedelta(hours = user_timeinterval)
            weekday = transfered_date.isoweekday()
            hour = transfered_date.hour
            pool_list = Timetable.objects.filter(day=weekday, start_time__gte=date, end_time__lt=time(hour))
            return render(request, 'swimapp/pool.html', {'pool_list': pool_list})
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def instantview(request):
    return render(request, 'swimapp/pool.html', {})
