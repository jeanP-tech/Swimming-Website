from django import forms
from datetime import datetime, date
from .models import City, Pool, TimeInterval
from django.forms import ModelChoiceField, ChoiceField
from django.forms.widgets import RadioSelect

class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=City.objects.all(),
        empty_label=None,
        )

    times = forms.ChoiceField(
        label='',
        choices=TimeInterval.TIME_CHOICES,
    )

    '''
    times = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=TimeInterval.objects.all(),
        empty_label=None,
        )
    '''

    class Meta:
        model = City
        fields = ['city_name',]
    '''
    class Meta:
        model = TimeInterval
        fields = ['time']
    '''
