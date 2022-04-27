from django.db import models

# Create your models here.

class hospitalinfo(models.Model):
    name= models.CharField(max_length=50)
    long= models.DecimalField(max_digits=10,decimal_places=7)
    lat= models.DecimalField(max_digits=9,decimal_places=7)
    address= models.CharField(max_length=200)
    review= models.TextField(null=True)
    rate=models.IntegerField(null=True)


class pharmacyinfo(models.Model):
    name= models.CharField(max_length=100)
    long= models.DecimalField(max_digits=10,decimal_places=7)
    lat= models.DecimalField(max_digits=9,decimal_places=7)
    address= models.CharField(max_length=200)
    review= models.TextField(null=True)
    rate=models.IntegerField(null=True)
