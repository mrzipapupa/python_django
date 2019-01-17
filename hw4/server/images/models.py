from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(
        max_length=150
    )
    value = models.ImageField()


    @property
    def url(self):
        return self.value.url

    def __str__(self):
        return self.name
