from django import forms
from .models import City, Pool, Price, Timetable, Userinfo

class SaveForm(forms.ModelForm):
    class Meta:
        model = Userinfo
        fields = ('user_info',)
