from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('pools/detail', views.detail, name = 'detail')
]
