from django import forms
from datetime import datetime
from .models import City, Pool, Userinfo
from django.forms import ModelChoiceField

class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        label='Which city do you want to swim?',
        required =True,
        queryset = City.objects.all(),
        empty_label=None,
        )

    class Meta:
        model = City, Userinfo,
        fields = ['city_name', 'user_city', 'user_time',]
