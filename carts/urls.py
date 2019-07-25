from django.urls import path

from .views import (
    cart_home,
    cart_update,
    cart_clear,
    checkout_home,
    reserve_home,
)

app_name = 'carts'
urlpatterns = [
    path('cart/', cart_home, name='home'),
    path('cart/checkout/', checkout_home, name='checkout'),
    path('cart/reserve/', reserve_home, name='reserve'),
    path('cart/update/', cart_update, name='update'),
    path('cart/clear/', cart_clear, name='clear'),
]
