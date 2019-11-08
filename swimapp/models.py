from django.db import models
from datetime import datetime

class City(models.Model):
    city_name = models.CharField(max_length = 20, default='')
    def __str__(self):
        return self.city_name

class Pool(models.Model):
    city = models.ForeignKey(City, default='', on_delete = models.CASCADE)
    pool_name = models.CharField(max_length = 30, default='')
    price = models.TextField(null=True)
    note = models.TextField(null=True)

    def __str__(self):
        return self.pool_name

class Timetable(models.Model):
    pool = models.ForeignKey(Pool, on_delete = models.CASCADE)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    # price = models.IntegerField(default=3500)

    DAY_CHOICES = [
        (1, "월요일"),
        (2, "화요일"),
        (3, "수요일"),
        (4, "목요일"),
        (5, "금요일"),
        (6, "토요일"),
        (7, "일요일"),
    ]
    day = models.IntegerField(
        choices = DAY_CHOICES,
        default = 1,
    )

    def __str__(self):
        title = '{0.pool} {0.day} {0.start_time}'
        return title.format(self)

class TimeInterval(models.Model):

    TIME_CHOICES = (
        ('', ' '),
        (3, "3시간"),
        (7, "7시간"),
        (12, "12시간"),
        (24, "24시간")
    )
