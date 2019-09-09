from django.db import models 

from django.contrib.auth.models import User
from django.core.validators import URLValidator


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return f"{self.name} {self.website}"
    
    
class ShoeType(models.Model):
    style = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.style}"
    
    
class ShoeColor(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.color_name}"


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete =models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type=models.CharField(max_length=30)
   
   
    def __str__(self):
        return f"{self.size}"
    