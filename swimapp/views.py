from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import datetime

def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            obj = Userinfo()
            obj.user_city = form.cleaned_data['cities']
            obj.user_time = datetime.now()
            obj.user_timeinterval = form.cleaned_data['times']
            obj.save()

            return HttpResponseRedirect('')
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})
