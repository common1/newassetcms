from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import Country


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'created_by', 'created_at',
                    'last_modified_by', 'last_modified_at')
