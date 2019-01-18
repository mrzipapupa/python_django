from django.db import models
from django.conf import settings
from products.models import Product
from utility.models import DateTimeManager


# Create your models here.

class Basket(DateTimeManager, models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='count', default=0)

