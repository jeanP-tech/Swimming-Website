from django import forms
from datetime import datetime, date
from .models import City, TimeInterval
from django.forms import ModelChoiceField, ChoiceField

class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=City.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'city_select'})
        #widget= forms.Select(attrs={'class':'city_form'}),
        )

    times = forms.ChoiceField(
        label='',
        choices=TimeInterval.TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'time_select'})
    )

    class Meta:
        model = City
        fields = ['city_name',]
