from django.urls import path

from . import views

app_name = 'siunits'
urlpatterns = [
    path('sibaseunits/',
         views.IndexView.as_view(), name='index_sibaseunits'),
    path('sibaseunits/create/',
         views.SiBaseUnitCreateView.as_view(), name='create_sibaseunit'),
    path('sibaseunits/<int:pk>/',
         views.SiBaseUnitUpdateView.as_view(), name='update_sibaseunit'),
    path('sibaseunits/read/<int:pk>',
         views.SiBaseUnitReadView.as_view(), name='read_sibaseunit'),
    path('sibaseunits/delete/<int:pk>',
         views.SiBaseUnitDeleteView.as_view(), name='delete_sibaseunit'),
]
