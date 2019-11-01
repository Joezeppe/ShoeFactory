from django.db import models

# Create your models here.


class Category(models.Model):
    CategoryName = models.CharField(max_length=50)
    Description = models.CharField(max_length=300)
    Picture = models.ImageField(upload_to='CategoryImages')
    Active = models.BooleanField()


class Product(models.Model):
    ProductName = models.CharField(max_length=35, null=False)
    ProductSKU = models.IntegerField(null=False)
    ProductDescription = models.CharField(max_length=250, null=True)
    CategoryID = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, default=1)
    QuantityPerUnit = models.IntegerField()
    MSRP = models.IntegerField( null=True)
    AvailableSize = models.CharField(max_length=20, blank=True)
    AvailableColor = models.CharField(max_length=20, blank=True)
    Size = models.CharField(max_length=20, blank=True)
    Color = models.CharField(max_length=20, blank=True)
    Discount = models.IntegerField(null=True)
    UnitWeight = models.IntegerField( null=True)
    UnitsInStock = models.IntegerField( null=True)
    UnitsOnOrder = models.IntegerField( null=True)
    UnitPrice = models.IntegerField( null=True)
    Picture = models.ImageField(upload_to='images/')
    Ranking = models.IntegerField( null=True)
    Note = models.CharField(max_length=300, null=True)
    # The reorder point is the level of inventory which triggers an action to
    # replenish that particular inventory stock. It is a minimum amount of an
    # item which a firm holds in stock, such that, when stock falls to this amount,
    # the item must be reordered
    ReorderLevel = models.IntegerField(null=False)


