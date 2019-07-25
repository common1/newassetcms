from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import Country


class CountryForm(BSModalForm):
    class Meta:
        model = Country
        fields = [
            'code',
            'name'
        ]
        labels = {
            'code': 'Code',
            'name': 'Name',
        }
