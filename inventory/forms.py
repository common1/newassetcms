from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import *


class AssetTypeForm(BSModalForm):
    class Meta:
        model = AssetType
        fields = [
            'shortcut',
            'name',
            'info',
        ]
        labels = {
            'shortcut': 'Shortcut',
            'name': 'Name',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class AssetForm(BSModalForm):
    class Meta:
        model = Asset
        fields = [
            'image',
            'name',
            'code',
            'assettype',
            'serial_number',
            'order_number',
            'purchase_date',
            'purchase_price',
            'supplier',
            'owner',
            'controller',
            'location',
            'lemma',
            'info',
        ]
        labels = {
            'image': 'Image',
            'name': 'Name',
            'code': 'Code',
            'assettype': 'Asset Type',
            'serial_number': 'Serial Number',
            'order_number': 'Order Number',
            'purchase_date': 'Purchase Date',
            'purchase_price': 'Purchase Price',
            'supplier': 'Supplier',
            'owner': 'Owner',
            'controller': 'Controller',
            'location': 'Location',
            'lemma': 'Lemma',
            'info': 'Info',
        }
        widgets = {
            'lemma': forms.Textarea(attrs={'rows': 2}),
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class ReservationForm(BSModalForm):
    class Meta:
        model = Reservation
        fields = [
            'name',
            'consumer',
            'title',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'info',
        ]
        labels = {
            'name': 'Name',
            'consumer': 'Consumer',
            'title': 'Title',
            'start_date': 'Start Date',
            'start_time': 'Start Time',
            'end_date': 'End Date',
            'end_time': 'End Time',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class ReservedAssetForm(BSModalForm):
    class Meta:
        model = ReservedAsset
        fields = [
            'reservation',
            'asset',
            'name',
            'info',
        ]
        labels = {
            'reservation': 'Reservation',
            'asset': 'Asset',
            'name': 'Name',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class LoanedAssetForm(BSModalForm):
    class Meta:
        model = LoanedAsset
        fields = [
            'reservedasset',
            'supplier_out',
            'receiver_out',
            'pickup_date',
            'pickup_time',
            'info',
        ]
        labels = {
            'reservedasset': 'Reserved Asset',
            'supplier_out': 'Supplier Out',
            'receiver_out': 'Receiver Out',
            'pickup_date': 'Pickup Date',
            'pickup_time': 'Pickup Time',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class ReturnedAssetForm(BSModalForm):
    class Meta:
        model = ReturnedAsset
        fields = [
            'loanedasset',
            'supplier_in',
            'receiver_in',
            'deliver_date',
            'deliver_time',
            'info',
        ]
        labels = {
            'loanedasset': 'Loaned Asset',
            'supplier_in': 'Supplier In',
            'receiver_in': 'Receiver In',
            'deliver_date': 'Deliver Date',
            'deliver_time': 'Deliver Time',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }
