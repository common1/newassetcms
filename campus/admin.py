from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import (
    Faculty,
    Building,
    Location,
    Section,
)


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0


@admin.register(Faculty)
class FacultyAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('css/custom_admin.css', )  # Include extra css
        }
    inlines = [SectionInline]
    list_display = ('code', 'name', 'created_by', 'created_at',
                    'last_modified_by', 'last_modified_at')


class LocationInline(admin.TabularInline):
    model = Location
    exclude = ['info']
    extra = 0


@admin.register(Building)
class BuildingAdmin(ImportExportModelAdmin):
    class Media:
        css = {
            'all': ('css/custom_admin.css', )     # Include extra css
        }
    inlines = [LocationInline]
    list_display = ('name', 'code', 'created_by', 'created_at',
                    'last_modified_by', 'last_modified_at')


@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin):
    list_display = ('room', 'building', 'created_by',
                    'created_at', 'last_modified_by', 'last_modified_at')


@admin.register(Section)
class SectionAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'faculty', 'created_by',
                    'created_at', 'last_modified_by', 'last_modified_at')
