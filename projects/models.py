from django.db import models
# from django.contrib.auth.models import User

from base.models import BaseModel
from inventory.models import Reservation

class Project(BaseModel):
    name = models.CharField(max_length=64)
    manager = models.ForeignKey('auth.User', related_name='manager', on_delete=models.CASCADE)
    staff = models.ManyToManyField('auth.User', related_name='staff')
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("projects:read_project", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

class ProjectReservation(BaseModel):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Project Reservations'
        ordering = ('name',)

    def __str__(self):
        return self.name
