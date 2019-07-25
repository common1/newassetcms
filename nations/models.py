from django.db import models
from django.urls import reverse

from base.models import BaseModel

# Country


class Country(BaseModel):
    code = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '{name} ( {code} )'.format(name=self.name, code=self.code)

    def get_absolute_url(self):
        return reverse('nations:countries_detail', kwargs={'id': self.id})
