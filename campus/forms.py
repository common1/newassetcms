from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import (
    Faculty,
    Building,
    Location,
    Section,
)


class FacultyForm(BSModalForm):
    class Meta:
        model = Faculty
        fields = [
            'code',
            'name'
        ]
        labels = {
            'code': 'code',
            'name': 'name',
        }


class BuildingForm(BSModalForm):
    class Meta:
        model = Building
        fields = [
            'code',
            'name',
            'info'
        ]
        labels = {
            'code': 'code',
            'name': 'name',
            'info': 'info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class LocationForm(BSModalForm):
    class Meta:
        model = Location
        fields = [
            'building',
            'room',
            'info'
        ]
        labels = {
            'building': 'building',
            'room': 'room',
            'info': 'info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }


class SectionForm(BSModalForm):
    class Meta:
        model = Section
        fields = [
            'code',
            'name',
            'faculty',
            'info'
        ]
        labels = {
            'code': 'code',
            'name': 'name',
            'faculty': 'faculty',
            'info': 'info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }
