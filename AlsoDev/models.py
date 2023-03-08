from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField('ProductImage', related_name='products')


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images')


class ProductCharacteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
