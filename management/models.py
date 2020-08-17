from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)


    def __str__(self):
       return self.name


class Dish(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    title=models.CharField(max_length=100,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    mrp=models.IntegerField(blank=True,null=True)
    img1=models.FileField(blank=True,null=True)
    img2=models.FileField(blank=True,null=True)
    img3=models.FileField(blank=True,null=True)
    dis=models.TextField(blank=True,null=True)
    avail=models.BooleanField(blank=True,null=True,default=True)


    def __str__(self):
        return self.title+ '-----'+ str(self.cat.name)


class Team(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    img=models.FileField(blank=True,null=True)
    fb=models.URLField(blank=True,null=True)
    tu=models.URLField(blank=True,null=True)
    insta=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name


