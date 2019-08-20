from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinfo, name='index'),
    #path('pools/detail', views.saveinfo, name = 'saveinfo'),
]
