from django.db.models import CharField
from django.db.models import TextField
from django.utils import timezone
from django.db import models as models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default='')
    images = models.ImageField(upload_to="static/img")
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    version = models.IntegerField(default=1)

    def __str__(self):
        return self.id