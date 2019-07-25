from django.db import models
from django.urls import reverse

from base.models import BaseModel

# See also:
# https://en.wikipedia.org/wiki/International_System_of_Units#Derived_units


class SiBaseUnit(BaseModel):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, unique=True)
    symbol = models.CharField(max_length=6, null=True, blank=True)
    dimension_symbol = models.CharField(max_length=6, null=True, blank=True)
    quantity_name = models.CharField(max_length=32, null=True, blank=True)
    value = models.FloatField(default=1.0)
    weight = models.FloatField(null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'SI Base Units'
        ordering = ('name',)

    def __str__(self):
        return '{name} ( {symbol} )'.format(name=self.name, symbol=self.symbol)

    def get_absolute_url(self):
        return reverse('siunits:sibaseunits_detail', kwargs={'id': self.id})
