from django.urls import path

from . import views

app_name = 'market'
urlpatterns = [
    path('suppliers/',
         views.SuppliersIndexView.as_view(), name='index_suppliers'),
    path('suppliers/create/',
         views.SupplierCreateView.as_view(), name='create_supplier'),
    path('suppliers/update/<int:pk>',
         views.SupplierUpdateView.as_view(), name='update_supplier'),
    path('suppliers/read/<int:pk>',
         views.SupplierReadView.as_view(), name='read_supplier'),
    path('suppliers/delete/<int:pk>',
         views.SupplierDeleteView.as_view(), name='delete_supplier'),
]
