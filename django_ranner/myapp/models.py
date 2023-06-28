from django.db import models
from PIL import Image
from django.db.models import TimeField


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    dec = models.TextField()

    def __str__(self):
        return self.name


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=5)

    def __str__(self):
        return self.name

# models.py
from django.db import models

class Cart(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
