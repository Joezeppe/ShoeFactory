from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    color = models.CharField(max_length=10)
    size = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    fabric = models.CharField(max_length=20)
    designer = models.CharField(max_length=16)
    image = models.ImageField(upload_to='images/')

    ProductName = models.CharField(max_length=35)
    ProductDescription = models.CharField(max_length=250)
    CategoryID = models.ForeignKey()
    QuantityPerUnit = models.IntegerField()
    UnitPrice = models.IntegerField()





