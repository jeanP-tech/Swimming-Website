from django.shortcuts import render
from .models import City, Pool, Timetable, TimeInterval
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
            pool_list = Pool.objects.filter(city=user_city)

            if hour >= 24:
                if weekday == 1:
                    time_list = Timetable.objects.filter(pool__in=pool_list, day=7, start_time__gte=date.time(), end_time__lte=time(23,59,59)) | Timetable.objects.filter(day=1, start_time__gte=time(0,0,0), end_time__lt=transfered_date.time())
                else:
                    time_list = Timetable.objects.filter(Q(pool__in=pool_list, day=weekday-1, start_time__gte=date.time(), end_time__lte=time(23,59,59)) | Q(pool__in=pool_list, day=weekday, start_time__gte=time(0,0,0), end_time__lt=transfered_date.time()))
            else:
                time_list = Timetable.objects.filter(pool__in=pool_list, day=weekday, start_time__gte=date.time(), end_time__lt=transfered_date.time())

            return render(request, 'swimapp/pool.html', {'pool_list': pool_list, 'time_list': time_list})
    else:
        form = CheckForm()
        return render(request, 'swimapp/index.html', {'form':form})
#
# def instantview(request):
#     return render(request, 'swimapp/pool.html', {})
