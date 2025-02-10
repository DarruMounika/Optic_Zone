from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User



class login(models.Model):
    username=models.CharField(max_length=20)
    password=models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='products/', null=True)
    category = models.CharField(max_length=50, choices=[('Sunglasses', 'Sunglasses'), ('Eyeglasses', 'Eyeglasses')], null=True)

    def __str__(self):
        return self.name
    



class Glasses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menglasses_images/')  # Store images in media folder

    def __str__(self):
        return self.name


class WGlasses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='womenglasses_images/')  

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE, null=True, blank=True)
    wglasses = models.ForeignKey(WGlasses, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)  # Track quantity

    def __str__(self):
        return f"Cart Item: {self.product or self.glasses or self.wglasses} - User: {self.user.username}"

