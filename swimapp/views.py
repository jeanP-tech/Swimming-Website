from django.shortcuts import render
from .models import City, Pool, Price, Timetable
from django.http import Http404

import datetime

def index(request):
    return render(request, 'swimapp/index.html', {})

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    latest_pool_list = Pool.objects.all()
    context = {'latest_pool_list': latest_pool_list}
    return render(request, 'swimapp/index.html', context)

def detail(request, pool_id):
    pool = get_object_or_404(Pool, pk=pool_id)
    return render(request, 'swimapp/detail.html', {'pool': pool})
