from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Supplier


class SupplierForm(BSModalForm):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'address',
            'postal_code',
            'town',
            'country',
            'phone_number',
            'fax_number',
            'email',
            'url',
            'info',
        ]
        labels = {
            'name': 'Name',
            'address': 'Address',
            'postal_code': 'Postal Code',
            'town': 'Town',
            'country': 'Country',
            'phone_number': 'Phone Number',
            'fax_number': 'Fax Number',
            'email': 'Email',
            'url': 'URL',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }
