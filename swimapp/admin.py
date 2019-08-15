from django.contrib import admin
from .models import City, Pool, Price, Timetable, Userinfo

admin.site.register(City)
admin.site.register(Pool)
admin.site.register(Price)
admin.site.register(Timetable)
admin.site.register(Userinfo)
