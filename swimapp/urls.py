from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.save_date, name = 'detail_page')
]
