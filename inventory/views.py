from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import *
from .models import *

from carts.models import AssetCart

# AssetType


class AssetTypesIndexView(generic.ListView):
    model = AssetType
    context_object_name = 'assettypes'
    template_name = 'inventory/assettypes/index.html'


class AssetTypeCreateView(BSModalCreateView):
    template_name = 'inventory/assettypes/create_assettype.html'
    form_class = AssetTypeForm
    success_message = 'Success: AssetType was created.'
    success_url = reverse_lazy('inventory:index_assettypes')


class AssetTypeUpdateView(BSModalUpdateView):
    model = AssetType
    template_name = 'inventory/assettypes/update_assettype.html'
    form_class = AssetTypeForm
    success_message = 'Success: AssetType was updated.'
    success_url = reverse_lazy('inventory:index_assettypes')


class AssetTypeReadView(BSModalReadView):
    model = AssetType
    template_name = 'inventory/assettypes/read_assettype.html'


class AssetTypeDeleteView(BSModalDeleteView):
    model = AssetType
    template_name = 'inventory/assettypes/delete_assettype.html'
    success_message = 'Success: AssetType was deleted.'
    success_url = reverse_lazy('inventory:index_assettypes')

# Asset

class AssetsFeaturedIndexView(generic.ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = 'inventory/assets/index.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Asset.objects.featured()

class AssetFeaturedReadView(BSModalReadView):
    model = Asset
    template_name = 'inventory/assets/read_featured_asset.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Asset.objects.featured()

class AssetsIndexView(generic.ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = 'inventory/assets/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AssetsIndexView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class AssetCreateView(BSModalCreateView):
    template_name = 'inventory/assets/create_asset.html'
    form_class = AssetForm
    success_message = 'Success: Asset was created.'
    success_url = reverse_lazy('inventory:index_assets')


class AssetUpdateView(BSModalUpdateView):
    model = Asset
    template_name = 'inventory/assets/update_asset.html'
    form_class = AssetForm
    success_message = 'Success: Asset was updated.'
    success_url = reverse_lazy('inventory:index_assets')


class AssetReadView(BSModalReadView):
    model = Asset
    template_name = 'inventory/assets/read_asset.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AssetReadView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context


class AssetDeleteView(BSModalDeleteView):
    model = Asset
    template_name = 'inventory/assets/delete_asset.html'
    success_message = 'Success: Asset was deleted.'
    success_url = reverse_lazy('inventory:index_assets')


# Reservation

class ReservationsIndexView(generic.ListView):
    model = Reservation
    context_object_name = 'reservations'
    template_name = 'inventory/reservations/index.html'


class ReservationCreateView(BSModalCreateView):
    template_name = 'inventory/reservations/create_reservation.html'
    form_class = ReservationForm
    success_message = 'Success: Reservation was created.'
    success_url = reverse_lazy('inventory:index_reservations')


class ReservationUpdateView(BSModalUpdateView):
    model = Reservation
    template_name = 'inventory/reservations/update_reservation.html'
    form_class = ReservationForm
    success_message = 'Success: ReservationForm was updated.'
    success_url = reverse_lazy('inventory:index_reservations')

class ReservationEditView(generic.DetailView):
    model = Reservation
    template_name = 'inventory/reservations/edit_reservation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ReservationEditView, self).get_context_data(*args, **kwargs)
        reservation_id = context['reservation'].id
        reservedassets = ReservedAsset.objects.filter(reservation__id=reservation_id)
        context['reservedassets'] = reservedassets
        return context

    #     cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
    #     for asset in cart_obj.assets.all():
    #         if asset in reservedassets:
    #             print(asset)


    # def get_context_data(self, *args, **kwargs):
    #     context = super(ReservationEditView, self).get_context_data(*args, **kwargs)
    #     cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
    #     context['cart'] = cart_obj
    #     return context

class ReservationAddBasket(generic.DetailView):
    model = Reservation
    template_name = 'inventory/reservations/add_basket_reservation.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ReservationAddBasket, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = AssetCart.objects.new_or_get(self.request)
        if cart_obj:
            context['assets'] = cart_obj.assets.all()
        return context

def add_basket(request):
    reservation_id = request.POST.get('reservation_id')
    reservation_obj = Reservation.objects.get(id=reservation_id)
    cart_obj, new_obj = AssetCart.objects.new_or_get(request)
    # reserved_assets = ReservedAsset.objects.all()
    reserved_assets = ReservedAsset.objects.filter(reservation__id=reservation_id)
    if cart_obj is not None:
        # Add all items from cart
        if reserved_assets.count() == 0:
            for asset in cart_obj.assets.all():
                ReservedAsset.objects.create(
                    reservation=reservation_obj,
                    asset=asset,
                    name=asset.name
                )
        # Add non duplicate items from cart
        else:
            for asset in cart_obj.assets.all():
                found = False
                for reserved_asset in reserved_assets:
                    if reserved_asset.asset.id == asset.id:
                        found = True
                if not found:
                    ReservedAsset.objects.create(
                        reservation=reservation_obj,
                        asset=asset,
                        name=asset.name
                    )

    return redirect("/reservations/edit/{reservation_id}".format(reservation_id=reservation_id))

def clear_reserved_assets(request):
    reservation_id = request.POST.get('reservation_id')
    reservation_obj = Reservation.objects.get(id=reservation_id)
    reserved_assets = ReservedAsset.objects.filter(reservation=reservation_obj).delete()

    return redirect("/reservations/edit/{reservation_id}".format(reservation_id=reservation_id))

def delete_reserved_asset(request):
    reservation_id = request.POST.get('reservation_id')
    reservedasset_id = request.POST.get('reservedasset_id')
    reservation_obj = Reservation.objects.get(id=reservation_id)
    reserved_assets = ReservedAsset.objects.filter(id=reservedasset_id, reservation=reservation_obj).delete()
    
    return redirect("/reservations/edit/{reservation_id}".format(reservation_id=reservation_id))

class ReservationReadView(BSModalReadView):
    model = Reservation
    template_name = 'inventory/reservations/read_reservation.html'


class ReservationDeleteView(BSModalDeleteView):
    model = Reservation
    template_name = 'inventory/reservations/delete_reservation.html'
    success_message = 'Success: Reservation was deleted.'
    success_url = reverse_lazy('inventory:index_reservations')

# ReservedAsset


class ReservedAssetsIndexView(generic.ListView):
    model = ReservedAsset
    context_object_name = 'reservedassets'
    template_name = 'inventory/reservedassets/index.html'


class ReservedAssetCreateView(BSModalCreateView):
    template_name = 'inventory/reservedassets/create_reservedasset.html'
    form_class = ReservedAssetForm
    success_message = 'Success: ReservedAsset was created.'
    success_url = reverse_lazy('inventory:index_reservedassets')


class ReservedAssetUpdateView(BSModalUpdateView):
    model = ReservedAsset
    template_name = 'inventory/reservedassets/update_reservedasset.html'
    form_class = ReservedAssetForm
    success_message = 'Success: ReservedAsset was updated.'
    success_url = reverse_lazy('inventory:index_reservedassets')


class ReservedAssetReadView(BSModalReadView):
    model = ReservedAsset
    template_name = 'inventory/reservedassets/read_reservedasset.html'


class ReservedAssetDeleteView(BSModalDeleteView):
    model = ReservedAsset
    template_name = 'inventory/reservedassets/delete_reservedasset.html'
    success_message = 'Success: ReservedAsset was deleted.'
    success_url = reverse_lazy('inventory:index_reservedassets')

# LoanedAsset


class LoanedAssetsIndexView(generic.ListView):
    model = LoanedAsset
    context_object_name = 'loanedassets'
    template_name = 'inventory/loanedassets/index.html'


class LoanedAssetCreateView(BSModalCreateView):
    template_name = 'inventory/loanedassets/create_loanedasset.html'
    form_class = LoanedAssetForm
    success_message = 'Success: LoanedAsset was created.'
    success_url = reverse_lazy('inventory:index_loanedassets')


class LoanedAssetUpdateView(BSModalUpdateView):
    model = LoanedAsset
    template_name = 'inventory/loanedassets/update_loanedasset.html'
    form_class = LoanedAssetForm
    success_message = 'Success: LoanedAsset was updated.'
    success_url = reverse_lazy('inventory:index_loanedassets')


class LoanedAssetReadView(BSModalReadView):
    model = LoanedAsset
    template_name = 'inventory/loanedassets/read_loanedasset.html'


class LoanedAssetDeleteView(BSModalDeleteView):
    model = LoanedAsset
    template_name = 'inventory/loanedassets/delete_loanedasset.html'
    success_message = 'Success: LoanedAsset was deleted.'
    success_url = reverse_lazy('inventory:index_loanedassets')

# ReturnedAsset


class ReturnedAssetsIndexView(generic.ListView):
    model = ReturnedAsset
    context_object_name = 'returnedassets'
    template_name = 'inventory/returnedassets/index.html'


class ReturnedAssetCreateView(BSModalCreateView):
    template_name = 'inventory/returnedassets/create_returnedasset.html'
    form_class = ReturnedAssetForm
    success_message = 'Success: ReturnedAsset was created.'
    success_url = reverse_lazy('inventory:index_returnedassets')


class ReturnedAssetUpdateView(BSModalUpdateView):
    model = ReturnedAsset
    template_name = 'inventory/returnedassets/update_returnedasset.html'
    form_class = ReturnedAssetForm
    success_message = 'Success: ReturnedAsset was updated.'
    success_url = reverse_lazy('inventory:index_returnedassets')


class ReturnedAssetReadView(BSModalReadView):
    model = ReturnedAsset
    template_name = 'inventory/returnedassets/read_returnedasset.html'


class ReturnedAssetDeleteView(BSModalDeleteView):
    model = ReturnedAsset
    template_name = 'inventory/returnedassets/delete_returnedasset.html'
    success_message = 'Success: ReturnedAsset was deleted.'
    success_url = reverse_lazy('inventory:index_returnedassets')
