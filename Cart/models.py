from django.db import models
from decimal import Decimal


# Create your models here.
class Cart(models.Model):
    product_id = models.CharField(max_length=255, blank=False, default='', unique=True)
    name = models.CharField(max_length=255, blank=False, default='')
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
