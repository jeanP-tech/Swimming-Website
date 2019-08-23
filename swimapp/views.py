from django.shortcuts import render
from .models import City, Pool, Price, Timetable, Userinfo
from .forms import CheckForm
from django.http import HttpResponseRedirect

from datetime import datetime

'''
def index(request):
    form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})

def saveinfo(request):
    user_datetime = datetime.datetime.now()
    user_datetime.save()
    return render(request, 'swimapp/index.html')
'''
def getinfo(request):
    if request.method == 'POST':
        form = CheckForm(request.POST)
        if form.is_valid():
            #obj = Userinfo()
            #obj.user_city = form.cleaned_data['cities']
            #obj.user_time = datetime.now()
            #obj.save()
            user_city = request.POST.get('user_city','')
            user_time = datetime.now()
            userinfo_obj = Userinfo(user_city = user_city, user_time = user_time)
            userinfo_obj.save()
            return HttpResponseRedirect('')
    else:
        form = CheckForm()
    return render(request, 'swimapp/index.html', {'form':form})
