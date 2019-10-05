from django.urls import path
from . import views

urlpatterns = [
    path('', views.getinfo, name='index'),
    # path('swimapp/pool', views.instantview, name='pool'),
]
