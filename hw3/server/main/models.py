from django.db import models

# Create your models here.

class Images(models.Model):
    img = models.ImageField(upload_to="D:\\Учеба\\python_django\\hw3\\server\\main\\static\\media\\main")