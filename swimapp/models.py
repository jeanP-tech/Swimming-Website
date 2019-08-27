from django.db import models
from datetime import datetime

class City(models.Model):
    city_name = models.CharField(max_length = 20, default='')
    def __str__(self):
        return self.city_name

class Pool(models.Model):
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    pool_name = models.CharField(max_length = 30, default='')
    def __str__(self):
        return self.pool_name

class Price(models.Model):
    pool = models.ForeignKey(Pool, on_delete = models.CASCADE)
    age = models.CharField(max_length = 20)
    price = models.IntegerField()
    WEEKDAYS = 'WEEK'
    WEEKENDS = 'WEEKENDS'
    WEEK_CHOICES = [
        (WEEKDAYS, 'Weekdays'),
        (WEEKENDS, 'Weekends'),
    ]
    week = models.CharField(
        max_length=10,
        choices=WEEK_CHOICES,
        default=WEEKDAYS,
    )

class Timetable(models.Model):
    pool = models.ForeignKey(Pool, on_delete = models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    DAY_CHOICES = [
        (MONDAY, 1),
        (TUESDAY, 2),
        (WEDNESDAY, 3),
        (THURSDAY, 4),
        (FRIDAY, 5),
        (SATURDAY, 6),
        (SUNDAY, 7),
    ]
    day = models.IntegerField(
        choices = DAY_CHOICES,
        default = 1,
    )

class TimeInterval(models.Model):
    TIME_CHOICES = (
        (3, 3),
        (5, 5),
        (7, 7),
        (12, 12),
    )


class Userinfo(models.Model):
    user_city = models.CharField(max_length = 20)
    user_time = models.DateTimeField(auto_now=False, auto_now_add=False, default=datetime.now())
    user_timeinterval = models.IntegerField(default=3)
    def __str__(self):
        return self.user_city
