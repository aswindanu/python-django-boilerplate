from django.contrib.auth.models import AbstractUser
from django.db import models as models


class User(AbstractUser):
    """
    Customize User django default model by inherit AbstractUser
    """
    phone_number = models.CharField(max_length=13, null=False, blank=False, unique=False)

    class Meta:
        db_table = 'auth_user'