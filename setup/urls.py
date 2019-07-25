"""newassetcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf.urls import include
from django.urls import path

from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view

urlpatterns = [
    path('', include('home.urls')),
    path('', include('samples.urls')),
    path('', include('nations.urls')),
    path('', include('siunits.urls')),
    path('', include('campus.urls')),
    path('', include('inventory.urls')),
    path('', include('projects.urls')),
    path('', include('market.urls')),
    path('', include('carts.urls')),
    path('login/', login_page, name='login'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register_page, name='register'),
    path('search/', include('search.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)