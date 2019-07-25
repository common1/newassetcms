from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'home'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='home/index.html')),
    path('', home_page, name='home'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='home/contact.html'), name='contact'),
    path('tables/', TemplateView.as_view(template_name='home/tables.html'), name='tables'),
]
