from django.db import models

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
    price_id = models.AutoField(primary_key=True)
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
    def __str__(self):
        return '%s %s' % (self.pool, self.price_id)

class Timetable(models.Model):
    pool = models.OneToOneField(Pool, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    DAY_CHOICES = [
        (MONDAY, 'MON'),
        (TUESDAY, 'TUE'),
        (WEDNESDAY, 'WED'),
        (THURSDAY, 'THU'),
        (FRIDAY, 'FRI'),
        (SATURDAY, 'SAT'),
        (SUNDAY, 'SUN'),
    ]
    day = models.CharField(
        max_length = 3,
        choices = DAY_CHOICES,
        default = MONDAY,
    )
