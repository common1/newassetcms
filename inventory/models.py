# Reservation
#   Asset
#
# Question

import random
import os
from django.db.models import Q
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.urls import reverse

# from django_currentuser.db.models import CurrentUserField
from base.models import (
    BaseModel,
)

from market.models import (
    Supplier,
)

from campus.models import (
    Section,
    Location
)

class AssetType(BaseModel):
    shortcut = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=64, unique=True)
    info = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Asset Types'
        ordering = ('name',)

    def __str__(self):
        return self.name

# Asset

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# def upload_assets_image_path_old(instance, filename):
#     new_filename = random.randint(1, 1000000000)
#     name, ext = get_filename_ext(filename)
#     final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
#     return "assets/{new_filename}/{final_filename}".format(
#         new_filename=new_filename, 
#         final_filename=final_filename
#         )

def upload_assets_image_path(instance, filename):
    new_filename = instance.id
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    print(new_filename)
    print(final_filename)
    return "assets/{new_filename}/{final_filename}".format(
        new_filename=new_filename, 
        final_filename=final_filename
        )

class AssetQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (
                    Q(name__icontains=query) | 
                    Q(info__icontains=query) |
                    Q(lemma__icontains=query) |
                    Q(purchase_price__icontains=query) |
                    Q(tag__title__icontains=query)
                  )
        return self.filter(lookups).distinct()
    
class AssetManager(models.Manager):
    def get_queryset(self):
        return AssetQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
            return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Asset(BaseModel):
    # name = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)
    code = models.CharField(max_length=12, blank=True)
    assettype = models.ForeignKey(     
        AssetType, related_name='asset_type', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=32, blank=True)
    order_number = models.CharField(max_length=32, blank=True)
    purchase_date = models.DateField(null=True,blank=True)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, related_name='supplier', on_delete=models.CASCADE)
    owner = models.ForeignKey(Section, null=True, blank=True, related_name='owner', on_delete=models.CASCADE)
    controller = models.ForeignKey(User, null=True, blank=True, related_name='controller', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, blank=True, related_name='location', on_delete=models.CASCADE)
    lemma = models.TextField(blank=True)
    image = models.ImageField(upload_to=upload_assets_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("inventory:read_asset", kwargs={"pk": self.pk})

    objects = AssetManager()

    class Meta:
        verbose_name_plural = 'Assets'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Reservation(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False)
    consumer = models.ForeignKey(
        'auth.User', related_name='reservation_consumer', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=128, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Reservations'
        ordering = ('-start_date',)

    def __str__(self):
        return self.name

    @property
    def reservedassets(self):
        return self.reservedasset_set.all()


class ReservedAsset(BaseModel):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    name = models.TextField(null=False, blank=False)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Reserved Assets'
        ordering = ('name',)

    def __str__(self):
        return self.name


class LoanedAsset(BaseModel):
    reservedasset = models.OneToOneField(
        ReservedAsset, on_delete=models.CASCADE)

    supplier_out = models.ForeignKey(
        'auth.User', null=True, blank=True, related_name='loanedasset_supplier_out', on_delete=models.CASCADE)
    receiver_out = models.ForeignKey(
        'auth.User', null=True, blank=True, related_name='loanedasset_receiver_out', on_delete=models.CASCADE)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Loaned Assets'

    # def __str__(self):
    #     return self.name


class ReturnedAsset(BaseModel):
    loanedasset = models.OneToOneField(LoanedAsset, on_delete=models.CASCADE)

    supplier_in = models.ForeignKey(
        'auth.User', null=True, blank=True, related_name='returnedasset_supplier_in', on_delete=models.CASCADE)
    receiver_in = models.ForeignKey(
        'auth.User', null=True, blank=True, related_name='returnedasset_receiver_in', on_delete=models.CASCADE)
    deliver_date = models.DateField(null=True, blank=True)
    deliver_time = models.TimeField(null=True, blank=True)

    info = models.TextField(blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Returned Assets'

    # def __str__(self):
    #     return self.name

