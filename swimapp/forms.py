from django import forms
from .models import City, pool, Price, Timetable, UserDate

class SaveForm(forms.ModelForm):
    class Meta:
        model = UserDate
        fields = ('user_datetime')
