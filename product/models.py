from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone
from django.db import models as models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=30, primary_key=True, unique=True)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default='')
    images = models.ImageField(upload_to="static/img")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.id