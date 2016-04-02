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