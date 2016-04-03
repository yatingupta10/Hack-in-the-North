from django.db import models
from django.utils import timezone


class Review(models.Model):
    No = models.IntegerField()
    Name = models.CharField(max_length=200)
    From = models.CharField(max_length=200)
    To = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Punctuality = models.FloatField()
    Food = models.FloatField()
    Crowd = models.FloatField()
    Services = models.FloatField()
    Cooling = models.FloatField()
    SeatAvailability = models.FloatField()

    def __str__(self):
        return self.Name

class Rank(models.Model):
    Source = models.CharField(max_length=200)
    Destination = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Delay(models.Model):
    Source = models.CharField(max_length=100)
    Destination = models.CharField(max_length=500)
    Delay = models.IntegerField()
    TrainNo = models.IntegerField()
    def __str__(self):
        return self.Name