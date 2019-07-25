from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import *


@admin.register(Supplier)
class SupplierAdmin(ImportExportModelAdmin):
    list_display = ('name', 'town', 'country', 'created_by',
                    'created_at', 'last_modified_by', 'last_modified_at')
    list_filter = ['town', 'country']
