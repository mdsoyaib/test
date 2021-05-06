from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
