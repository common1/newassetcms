import os
import json
import datetime
import random
from django.core.management.base import BaseCommand
from campus.models import Faculty, Building, Location, Section
from inventory.models import AssetType, Asset, Reservation
from market.models import Supplier
from nations.models import Country

def generate_start_date():
    year = random.randint(2020, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

def generate_end_date():
    year = random.randint(2022, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)

def generate_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return datetime.time(hour, minute)

# Campus
def create_faculties(self):
    Faculty.objects.get_or_create(code='B', name='Built Environment')

def create_buildings(self):
    Building.objects.get_or_create(code='V', name='Vertigo')

def create_locations(self):
    building = Building.objects.get(code='V')
    Location.objects.get_or_create(building=building, room='2.56')
    Location.objects.get_or_create(building=building, room='2.57')
    Location.objects.get_or_create(building=building, room='2.58')
    Location.objects.get_or_create(building=building, room='2.59')
    Location.objects.get_or_create(building=building, room='2.60')
    Location.objects.get_or_create(building=building, room='2.61')
    Location.objects.get_or_create(building=building, room='2.62')
    Location.objects.get_or_create(building=building, room='2.63')
    Location.objects.get_or_create(building=building, room='2.64')

def create_sections(self):
    faculty = Faculty.objects.get(code='B')
    Section.objects.get_or_create(code='BPS', name='Building Physics and Systems', faculty=faculty)
    Section.objects.get_or_create(code='IMS1', name='Imaginary Section 1', faculty=faculty)
    Section.objects.get_or_create(code='IMS2', name='Imaginary Section 2', faculty=faculty)
    Section.objects.get_or_create(code='IMS3', name='Imaginary Section 3', faculty=faculty)
    Section.objects.get_or_create(code='IMS4', name='Imaginary Section 4', faculty=faculty)
    Section.objects.get_or_create(code='IMS5', name='Imaginary Section 5', faculty=faculty)

# Nations
def create_countries(self):
    Country.objects.get_or_create(code='NL', name='Netherlands')
    Country.objects.get_or_create(code='BE', name='Belgium')
    Country.objects.get_or_create(code='GE', name='Germany')
    Country.objects.get_or_create(code='F', name='France')
    Country.objects.get_or_create(code='GB', name='Great Britain')
    Country.objects.get_or_create(code='IC1', name='Imaginary Country 1')
    Country.objects.get_or_create(code='IC2', name='Imaginary Country 2')
    Country.objects.get_or_create(code='IC3', name='Imaginary Country 3')
    Country.objects.get_or_create(code='IC4', name='Imaginary Country 4')
    Country.objects.get_or_create(code='IC5', name='Imaginary Country 5')

# Market
def create_suppliers(self):
    country = Country.objects.get(code='NL')
    Supplier.objects.get_or_create(
        name='First imaginary supplier', 
        town='Eindhoven', 
        country=country
    )
    Supplier.objects.get_or_create(
        name='Second imaginary supplier', 
        town='Eindhoven', 
        country=country
    )
    Supplier.objects.get_or_create(
        name='Third imaginary supplier', 
        town='Eindhoven', 
        country=country
    )
    Supplier.objects.get_or_create(
        name='Fourth imaginary supplier', 
        town='Eindhoven', 
        country=country
    )
    Supplier.objects.get_or_create(
        name='Fifth imaginary supplier', 
        town='Eindhoven', 
        country=country
    )

# Inventory
def create_asset_types(self):
    AssetType.objects.get_or_create(shortcut='V', name='Voltmeter')
    AssetType.objects.get_or_create(shortcut='A', name='Amperemeter')
    AssetType.objects.get_or_create(shortcut='IV1', name='Imaginary voltmeter 1')
    AssetType.objects.get_or_create(shortcut='IV2', name='Imaginary voltmeter 2')
    AssetType.objects.get_or_create(shortcut='IV3', name='Imaginary voltmeter 3')
    AssetType.objects.get_or_create(shortcut='IV4', name='Imaginary voltmeter 4')
    AssetType.objects.get_or_create(shortcut='IV5', name='Imaginary voltmeter 5')
    AssetType.objects.get_or_create(shortcut='IA1', name='Imaginary amperemeter 1')
    AssetType.objects.get_or_create(shortcut='IA2', name='Imaginary amperemeter 2')
    AssetType.objects.get_or_create(shortcut='IA3', name='Imaginary amperemeter 3')
    AssetType.objects.get_or_create(shortcut='IA4', name='Imaginary amperemeter 4')
    AssetType.objects.get_or_create(shortcut='IA5', name='Imaginary amperemeter 5')

def create_assets(self):
    assettype = AssetType.objects.get(shortcut='IV1')
    supplier = Supplier.objects.get(name='First imaginary supplier')
    section = Section.objects.get(code='IMS1')
    Asset.objects.get_or_create(
        name='First Voltmeter', 
        code='', 
        assettype=assettype,
        serial_number='',
        order_number='',
        supplier=supplier,
        owner=section   
    )
    Asset.objects.get_or_create(
        name='Second Voltmeter', 
        code='', 
        assettype=assettype,
        serial_number='',
        order_number='',
        supplier=supplier,
        owner=section   
    )
    Asset.objects.get_or_create(
        name='Third Voltmeter', 
        code='', 
        assettype=assettype,
        serial_number='',
        order_number='',
        supplier=supplier,
        owner=section   
    )
    Asset.objects.get_or_create(
        name='Fourth Voltmeter', 
        code='', 
        assettype=assettype,
        serial_number='',
        order_number='',
        supplier=supplier,
        owner=section   
    )
    Asset.objects.get_or_create(
        name='Fifth Voltmeter', 
        code='', 
        assettype=assettype,
        serial_number='',
        order_number='',
        supplier=supplier,
        owner=section   
    )

def create_reservations(self):
    Reservation.objects.get_or_create(
        name='First Imaginary Reservation',
        start_date=generate_start_date(),
        end_date=generate_end_date(),
        start_time=generate_time(),
        end_time=generate_time()
    )
    Reservation.objects.get_or_create(
        name='Second Imaginary Reservation',
        start_date=generate_start_date(),
        end_date=generate_end_date(),
        start_time=generate_time(),
        end_time=generate_time()
    )
    Reservation.objects.get_or_create(
        name='Third Imaginary Reservation',
        start_date=generate_start_date(),
        end_date=generate_end_date(),
        start_time=generate_time(),
        end_time=generate_time()
    )
    Reservation.objects.get_or_create(
        name='Fourth Imaginary Reservation',
        start_date=generate_start_date(),
        end_date=generate_end_date(),
        start_time=generate_time(),
        end_time=generate_time()
    )
    Reservation.objects.get_or_create(
        name='Fifth Imaginary Reservation',
        start_date=generate_start_date(),
        end_date=generate_end_date(),
        start_time=generate_time(),
        end_time=generate_time()
    )

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Campus
        create_faculties(self)
        create_buildings(self)
        create_locations(self)
        create_sections(self)

        # Market
        create_suppliers(self)

        # Nations
        create_countries(self)

        # Inventory
        create_asset_types(self)
        create_assets(self)
        create_reservations(self)

        self.stdout.write(self.style.SUCCESS('Inventory objects successfully created'))
