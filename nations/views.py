from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import CountryForm
from .models import Country


class IndexView(generic.ListView):
    model = Country
    context_object_name = 'countries'
    template_name = 'nations/countries/index.html'


class CountryCreateView(BSModalCreateView):
    template_name = 'nations/countries/create_country.html'
    form_class = CountryForm
    success_message = 'Success: Country was created.'
    success_url = reverse_lazy('nations:index_countries')


class CountryUpdateView(BSModalUpdateView):
    model = Country
    template_name = 'nations/countries/update_country.html'
    form_class = CountryForm
    success_message = 'Success: Country was updated.'
    success_url = reverse_lazy('nations:index_countries')


class CountryReadView(BSModalReadView):
    model = Country
    template_name = 'nations/countries/read_country.html'


class CountryDeleteView(BSModalDeleteView):
    model = Country
    template_name = 'nations/countries/delete_country.html'
    success_message = 'Success: Country was deleted.'
    success_url = reverse_lazy('nations:index_countries')
