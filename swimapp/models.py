from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length = 20, default='DEFAULT VALUE')

class Pool(models.Model):
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)

'''
class Price(models.Model):
    pool = models.OneToOneField(Pool, on_delete = models.CASCADE)
    age = models.CharField(max_length = 20)
    price = models.IntegerField()

class Timetable(models.Model):
    pool = models.OneToOneField(Pool, on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
'''
