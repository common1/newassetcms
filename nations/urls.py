from django.urls import path

from . import views

app_name = 'nations'
urlpatterns = [
    path('countries/',
         views.IndexView.as_view(), name='index_countries'),
    path('countries/create/',
         views.CountryCreateView.as_view(), name='create_country'),
    path('countries/update/<int:pk>',
         views.CountryUpdateView.as_view(), name='update_country'),
    path('countries/read/<int:pk>',
         views.CountryReadView.as_view(), name='read_country'),
    path('countries/delete/<int:pk>',
         views.CountryDeleteView.as_view(), name='delete_country'),
]
