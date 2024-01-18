from django.db import models

# Create your models here.
class User(models.Model):
    fullName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phoneNo = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class TravelPlan(models.Model):
    place = models.CharField(max_length=30)
    date = models.DateField()
    end_date = models.DateField()
    des = models.CharField(max_length=300)
    cost = models.CharField(max_length=30)
    member = models.CharField(max_length=3)

class Booking(models.Model):
    userId = models.CharField(max_length=30)
    travelPlanId = models.CharField(max_length=30)
    bookingId = models.CharField(max_length=30)
    cost = models.CharField(max_length=8)
    member = models.CharField(max_length=30)
    