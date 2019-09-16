from django.contrib import admin
from .models import City, Pool, Price, Timetable, TimeInterval

admin.site.register(City)
admin.site.register(Pool)
admin.site.register(Price)
admin.site.register(Timetable)
admin.site.register(TimeInterval)
