from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import SiBaseUnitForm
from .models import SiBaseUnit


class IndexView(generic.ListView):
    model = SiBaseUnit
    context_object_name = 'sibaseunits'
    template_name = 'siunits/sibaseunits/index.html'


class SiBaseUnitCreateView(BSModalCreateView):
    template_name = 'siunits/sibaseunits/create_sibaseunit.html'
    form_class = SiBaseUnitForm
    success_message = 'Success: SI Base Unit was created.'
    success_url = reverse_lazy('siunits:index_sibaseunits')


class SiBaseUnitUpdateView(BSModalUpdateView):
    model = SiBaseUnit
    template_name = 'siunits/sibaseunits/update_sibaseunit.html'
    form_class = SiBaseUnitForm
    success_message = 'Success: SI Base Unit was updated.'
    success_url = reverse_lazy('siunits:index_sibaseunits')


class SiBaseUnitReadView(BSModalReadView):
    model = SiBaseUnit
    template_name = 'siunits/sibaseunits/read_sibaseunit.html'


class SiBaseUnitDeleteView(BSModalDeleteView):
    model = SiBaseUnit
    template_name = 'siunits/sibaseunits/delete_sibaseunit.html'
    success_message = 'Success: SI Base Unit was deleted.'
    success_url = reverse_lazy('siunits:index_sibaseunits')
