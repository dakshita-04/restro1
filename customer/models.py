from django.db import models
from .states import States
from django.contrib.auth.models import User
from datetime import date
from management.models import Dish

class Add_to_cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,)
    dish=models.ForeignKey(Dish,on_delete=models.CASCADE,blank=True, null=True,)
    qty=models.IntegerField(blank=True, null=True)
    confirm=models.BooleanField(blank=True, null=True, default=True)

    def __str__(self):
     return self.user.username






class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    HouseNum = models.CharField(max_length=15,blank=True, null=True)
    Area = models.CharField(blank=True, null=True, max_length=50)
    City = models.CharField(blank=True, null=True, max_length=30)
    District = models.CharField(blank=True, null=True,max_length=50)
    State = models.CharField(null=True,blank=True, choices=States, max_length=45)
    pin = models.IntegerField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.user.username


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(null=True, blank=True, max_length=30)
    mob = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    guest = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6)], blank=True, null=True)
    date = models.DateField(blank=True, null=True, default=date.today)
    time = models.TimeField(blank=True, null=True)
    confirm = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name + ' <---> ' + str(self.date) + ' <---> ' + str(self.time)

