from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accountuser(AbstractUser):
    avatar = models.ForeignKey(
        'images.Image',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        max_length=11,
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username