from django.shortcuts import render, redirect

from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail

from addresses.forms import AddressForm
from addresses.models import Address

from billing.models import BillingProfile
from orders.models import AssetOrder
from inventory.models import Asset
from .models import AssetCart


def cart_home(request):
    cart_obj, new_obj = AssetCart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})

def cart_update(request):
    asset_id = request.POST.get('asset_id')
    current = request.POST.get('current')
    if asset_id is not None:
        try:
            asset_obj = Asset.objects.get(id=asset_id)
        except Asset.DoesNotExists:
            return redirect("inventory:index_assets")

        cart_obj, new_obj = AssetCart.objects.new_or_get(request)
        if asset_obj in cart_obj.assets.all():
            cart_obj.assets.remove(asset_obj)
        else:
            cart_obj.assets.add(asset_obj)
        request.session['cart_items'] = cart_obj.assets.count()
    if current == 'carts':
        return redirect("carts:home")
    if current == 'assets':
        return redirect("inventory:index_assets")
    if current == 'search':
        query = request.POST.get('query')
        response = redirect("search:query")
        response['Location'] += '?q={query}'.format(query=query)
        return response

def cart_clear(request):
    cart_obj, new_obj = AssetCart.objects.new_or_get(request)
    if cart_obj:
        for asset_obj in cart_obj.assets.all():
            cart_obj.assets.remove(asset_obj)
        request.session['cart_items'] = 0
    return redirect("carts:home")
   

def reserve_home(request):
    context = {
        
    }
    return render(request, "carts/reserve.html", context)

def checkout_home(request):
    cart_obj, cart_created = AssetCart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.assets.count() == 0:
        return redirect("carts:home")

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    billing_address_id = request.session.get("billing_address_id", None)
    shipping_address_id = request.session.get("shipping_address_id", None)
    
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)

    if billing_profile is not None:
        order_obj, order_obj_created = AssetOrder.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            del request.session["shipping_address_id"]
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session["billing_address_id"]
        if billing_address_id or shipping_address_id:
            order_obj.save()            

    if request.method == "POST":
        print("Inside Method POST")
        is_done = order_obj.check_done()
        if is_done:
            order_obj.mark_paid()
            request.session['cart_items'] = 0
            del request.session['cart_id']
            return redirect("/cart/success")

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form,
        "address_form": address_form,
    }
    return render(request, "carts/checkout.html", context)
