from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import SupplierForm
from .models import Supplier


class SuppliersIndexView(generic.ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'market/suppliers/index.html'


class SupplierCreateView(BSModalCreateView):
    template_name = 'market/suppliers/create_supplier.html'
    form_class = SupplierForm
    success_message = 'Success: Supplier was created.'
    success_url = reverse_lazy('market:index_suppliers')


class SupplierUpdateView(BSModalUpdateView):
    model = Supplier
    template_name = 'market/suppliers/update_supplier.html'
    form_class = SupplierForm
    success_message = 'Success: Supplier was updated.'
    success_url = reverse_lazy('market:index_suppliers')


class SupplierReadView(BSModalReadView):
    model = Supplier
    template_name = 'market/suppliers/read_supplier.html'


class SupplierDeleteView(BSModalDeleteView):
    model = Supplier
    template_name = 'market/suppliers/delete_supplier.html'
    success_message = 'Success: Supplier was deleted.'
    success_url = reverse_lazy('market:index_suppliers')
