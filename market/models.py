from django.db import models

from base.models import BaseModel
from nations.models import Country

# Create your models here.


class Supplier(BaseModel):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64, blank=True)
    postal_code = models.CharField(max_length=12, blank=True)
    town = models.CharField(max_length=48, blank=True)
    country = models.ForeignKey(
        Country, related_name='country', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=32, blank=True)
    fax_number = models.CharField(max_length=32, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    url = models.URLField(max_length=128, blank=True)
    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name
