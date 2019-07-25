from django import forms

from .models import Address
# TODO: Current 087 - 3:57
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'address_line1',
            'address_line2',
            'city',
            'country',
            'postal_code',
        ]
