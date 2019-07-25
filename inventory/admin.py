from django.contrib import admin

from .models import *

admin.site.register(AssetType)

class AssetAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'purchase_price', 'assettype', 'active']
    class Meta:
        model = Asset

admin.site.register(Asset, AssetAdmin)

admin.site.register(Reservation)
admin.site.register(ReservedAsset)
admin.site.register(LoanedAsset)
admin.site.register(ReturnedAsset)
