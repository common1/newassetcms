from django import forms

from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

from .models import *

class ProjectForm(BSModalForm):
    class Meta:
        model = Project
        fields = [
                'name',
                'manager',
                'staff',
                'start_date',
                'end_date',
                'info',
        ]
        labels = {
                'name': 'Name',
                'manager': 'Manager',
                'staff': 'Staff',
                'start_date': 'Start Date',
                'end_date': 'End Date',
                'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }

class ProjectReservationForm(BSModalForm):
    class Meta:
        fields = [
            'reservation',
            'project',
            'name',
            'info',
        ]
        labels = {
            'reservation': 'Reservation',
            'project': 'Project',
            'name': 'Name',
            'info': 'Info',
        }
        widgets = {
            'info': forms.Textarea(attrs={'rows': 2}),
        }
