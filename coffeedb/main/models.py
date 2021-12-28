from django.db import models
from django.contrib.auth.models import AbstractUser

class CoffeeUser(AbstractUser):
    class Meta:
        verbose_name = 'CoffeeUser'
        verbose_name_plural = 'CoffeeUsers'
    id = models.AutoField(primary_key=True, unique=True)
    
    def __str__(self):
        """Return givenname and surname."""
        return (f"{self.first_name} {self.last_name}")


class Product(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=255,unique=True)
    description = models.CharField(max_length=255,unique=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to="image",null=True,blank=True)

    def __str__(self):
        return self.name