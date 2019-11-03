from django import forms
from datetime import datetime, date
from .models import City, TimeInterval
from django.forms import ModelChoiceField

class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        label='',
        required=True,
        queryset=City.objects.all(),
        empty_label='',
        widget=forms.Select(attrs={'class': 'form_select'})
        )

    times = forms.ChoiceField(
        label='',
        choices=TimeInterval.TIME_CHOICES,
        # empty_label='',
        widget=forms.Select(attrs={'class': 'form_select'})
    )

    class Meta:
        model = City
        fields = ['city_name']
