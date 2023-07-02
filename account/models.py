from django.db import models
from django.contrib.auth.models import User
from product.models import City

class UserCity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='شهر')

    def __str__(self):
        return self.city.name
