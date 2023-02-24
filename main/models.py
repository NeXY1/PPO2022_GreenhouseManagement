from django.db import models


class Day(models.Model):
    DayID = models.BigAutoField(primary_key=True)
    Date = models.DateField()
    AverageT = models.IntegerField()
    AverageAH = models.IntegerField()
    AverageSH = models.IntegerField()

class Time(models.Model):
    TimeID = models.BigAutoField(primary_key=True)
    DayID = models.ForeignKey(Day, on_delete=models.CASCADE)
    Time = models.TextField()

class TemperatureValue(models.Model):
    DayID = models.ForeignKey(Day, on_delete=models.CASCADE)
    TimeID = models.ForeignKey(Time, on_delete=models.CASCADE)
    S1 = models.IntegerField()
    S2 = models.IntegerField()
    S3 = models.IntegerField()
    S4 = models.IntegerField()
    AverageT = models.IntegerField()

class AirHudimityValue(models.Model):
    DayID = models.ForeignKey(Day, on_delete=models.CASCADE)
    TimeID = models.ForeignKey(Time, on_delete=models.CASCADE)
    S1 = models.IntegerField()
    S2 = models.IntegerField()
    S3 = models.IntegerField()
    S4 = models.IntegerField()
    AverageT = models.IntegerField()

class SoilHudimityValue(models.Model):
    DayID = models.ForeignKey(Day, on_delete=models.CASCADE)
    TimeID = models.ForeignKey(Time, on_delete=models.CASCADE)
    S1 = models.IntegerField()
    S2 = models.IntegerField()
    S3 = models.IntegerField()
    S4 = models.IntegerField()
    AverageT = models.IntegerField()
