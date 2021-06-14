from django.db import models

# Create your models here.


class Shop(models.Model):
    
    shop_owner_name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.IntegerField()
    home_delievery = models.BooleanField(default=False)
    description = models.TextField()

class Shopimage(models.Model):
    
    image = models.ImageField(upload_to='static')
