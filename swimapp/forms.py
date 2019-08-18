from django import forms
from datetime import datetime
from .models import City, Pool, Price, Timetable, Userinfo
from django.forms import ModelChoiceField

class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        required =True,
        queryset = City.objects.all()
        )

    class Meta:
        model = City
        fields = ('city_name',)
