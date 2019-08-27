from datetime import datetime, timedelta
from .models import City, Pool, Price, Timetable, Userinfo

user_timeinterval = 6
hour = datetime.now().hour + user_timeinterval
if hour >= 24:
    hour -= 24
    day = datetime.now() + timedelta(days=1, hours=user_timeinterval) - timedelta(hours=24)
weekday = day.isoweekday()
Timetable.objects.get(Day=1)
