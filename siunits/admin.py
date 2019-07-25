from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import SiBaseUnit


@admin.register(SiBaseUnit)
class SiBaseUnitAdmin(ImportExportModelAdmin):
    list_display = ('name', 'symbol', 'dimension_symbol', 'quantity_name',
                    'value', 'weight', 'created_by', 'created_at',
                    'last_modified_by', 'last_modified_at')
