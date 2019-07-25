from django.db import models
from django.urls import reverse

from base.models import BaseModel

# Faculty


class Faculty(BaseModel):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return '{name} ( {code} )'.format(name=self.name, code=self.code)

    def get_absolute_url(self):
        return reverse('campus:faculties_detail', kwargs={'id': self.id})

# Building


class Building(BaseModel):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=48)
    info = models.TextField(blank=True)
    # avatar = models.ImageField(null=True, blank=True, upload_to='/avatar/building')

    class Meta:
        verbose_name_plural = 'Buildings'

    def __str__(self):
        return '{name} ( {code} )'.format(name=self.name, code=self.code)

    def get_absolute_url(self):
        return reverse('campus:buildings_detail', kwargs={'id': self.id})

# Location


class Location(BaseModel):
    building = models.ForeignKey(
        Building, related_name='building', on_delete=models.CASCADE)
    room = models.CharField(max_length=32, unique=True)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Locations'
        ordering = ['room']

    def __str__(self):
        return '{room} - {building}'.format(room=self.room, building=self.building)
        # return self.room

    def get_absolute_url(self):
        return reverse('campus:locations_detail', kwargs={'id': self.id})

# Section


class Section(BaseModel):
    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=128)
    faculty = models.ForeignKey(
        Faculty, related_name='faculty', on_delete=models.CASCADE)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Sections'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('campus:sections_detail', kwargs={'id': self.id})
