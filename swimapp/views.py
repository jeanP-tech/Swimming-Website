from django.shortcuts import render
from .models import City, Pool, Price, Timetable, TimeInterval
from .forms import CheckForm
from django.http import HttpResponseRedirect
from django.db.models import Q

from datetime import date, datetime, timedelta, time

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            user_city = form.cleaned_data['cities']
            user_timeinterval = int(form.cleaned_data['times'])
            date = datetime.now()
            transfered_date = date + timedelta(hours = user_timeinterval)
            weekday = transfered_date.isoweekday()
            hour = date.hour + user_timeinterval
            if hour >= 24:
                if weekday == 1:
                    pool_list = Timetable.objects.filter(day=7, start_time__gte=date.time(), end_time__lte=time(23,59,59)) | Timetable.objects.filter(day=1, start_time__gte=time(0,0,0), end_time__lt=transfered_date.time())
                    price_list = Price.objects.filter(week = 'WEEKENDS')
                else:
                    pool_list = Timetable.objects.filter(Q(day=weekday-1, start_time__gte=date.time(), end_time__lte=time(23,59,59)) | Q(day=weekday, start_time__gte=time(0,0,0), end_time__lt=transfered_date.time()))
                    if weekday <= 5:
                        w = 'WEEKDAYS'
                    else:
                        w = 'WEEKENDS'
                    price_list = Price.objects.filter(week = w)

            else:
                if weekday <= 5:
                    w = 'WEEKDAYS'
                else:
                    w = 'WEEKENDS'
                pool_list = Timetable.objects.filter(day=weekday, start_time__gte=date.time(), end_time__lt=transfered_date.time())
                price_list = Price.objects.filter(week = w)
            return render(request, 'swimapp/pool.html', {'pool_list': pool_list}, {'price_list': price_list})
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def instantview(request):
    return render(request, 'swimapp/pool.html', {})
