from django.db import models
from datetime import datetime


class City(models.Model):
    city_name = models.CharField(max_length = 20, default='')
    def __str__(self):
        return self.city_name

class Pool(models.Model):
    city = models.ForeignKey(City, default='', on_delete = models.CASCADE)
    pool_name = models.CharField(max_length = 30, default='')
    def __str__(self):
        return self.pool_name

class Price(models.Model):
    pool = models.ForeignKey(Pool, on_delete = models.CASCADE)
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

    YES = 'Y'
    NO = 'N'
    YN_CHOICES = [
        (YES, 'Y'),
        (NO, 'N'),
    ]
    registered = models.CharField(
        max_length=1,
        choices=YN_CHOICES,
        default=YES,
    )

    def __str__(self):
        title = '{0.pool} {0.week} {0.registered}'
        return title.format(self)

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

    def __str__(self):
        title = '{0.pool} {0.day} {0.start_time}'
        return title.format(self)

class Time(models.Model):
    time = models.IntegerField()
    def __str__(self):
        title = '{0.time}'
        return title.format(self)

class TimeInterval(models.Model):

    TIME_CHOICES = (
        (3, "3시간"),
        (7, "7시간"),
        (12, "12시간"),
    )
    #time = models.CharField(max_length=10, choices="TIME_CHOICES")
    '''
    time = models.IntegerField(default=0)
    time_name = models.CharField(max_length=10, default='')
    def __str__(self):
        title = '{0.time_name}'
        return title.format(self)
    '''
