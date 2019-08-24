from django import forms
from datetime import datetime
from .models import City, Pool, Userinfo, TimeInterval
from django.forms import ModelChoiceField, ChoiceField
from django.forms.widgets import RadioSelect



class CheckForm(forms.Form):
    cities = forms.ModelChoiceField(
        label='Which city do you want to swim?',
        required=True,
        queryset=City.objects.all(),
        empty_label=None,
        )

    times = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices = TimeInterval.TIME_CHOICES,
    )

    class Meta:
        model = City
        fields = ['city_name',]
