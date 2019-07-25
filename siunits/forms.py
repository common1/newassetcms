from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import SiBaseUnit


class SiBaseUnitForm(BSModalForm):
    class Meta:
        model = SiBaseUnit
        fields = [
            'parent',
            'name',
            'symbol',
            'dimension_symbol',
            'quantity_name',
            'value',
            'weight',
            'info',
        ]
        labels = {
            'parent': 'Parent',
            'name': 'Name',
            'symbol': 'Symbol',
            'dimension_symbol': 'Dimension Symbol',
            'quantity_name': 'Quantity Name',
            'value': 'Value',
            'weight': 'Weight',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }
