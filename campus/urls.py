from django.urls import path

from . import views

app_name= 'campus'
urlpatterns = [
    path('faculties/',
         views.FacultiesIndexView.as_view(), name='index_faculties'),
    path('faculties/create/',
         views.FacultyCreateView.as_view(), name='create_faculty'),
    path('faculties/update/<int:pk>',
         views.FacultyUpdateView.as_view(), name='update_faculty'),
    path('faculties/read/<int:pk>',
         views.FacultyReadView.as_view(), name='read_faculty'),
    path('faculties/delete/<int:pk>',
         views.FacultyDeleteView.as_view(), name='delete_faculty'),

    path('buildings/',
         views.BuildingsIndexView.as_view(), name='index_buildings'),
    path('buildings/create/',
         views.BuildingCreateView.as_view(), name='create_building'),
    path('buildings/update/<int:pk>',
         views.BuildingUpdateView.as_view(), name='update_building'),
    path('buildings/read/<int:pk>',
         views.BuildingReadView.as_view(), name='read_building'),
    path('buildings/delete/<int:pk>',
         views.BuildingDeleteView.as_view(), name='delete_building'),

    path('locations/',
         views.LocationsIndexView.as_view(), name='index_locations'),
    path('locations/create/',
         views.LocationCreateView.as_view(), name='create_location'),
    path('locations/update/<int:pk>',
         views.LocationUpdateView.as_view(), name='update_location'),
    path('locations/read/<int:pk>',
         views.LocationReadView.as_view(), name='read_location'),
    path('locations/delete/<int:pk>',
         views.LocationDeleteView.as_view(), name='delete_location'),

    path('sections/',
         views.SectionsIndexView.as_view(), name='index_sections'),
    path('sections/create/',
         views.SectionCreateView.as_view(), name='create_section'),
    path('sections/update/<int:pk>',
         views.SectionUpdateView.as_view(), name='update_section'),
    path('sections/read/<int:pk>',
         views.SectionReadView.as_view(), name='read_section'),
    path('sections/delete/<int:pk>',
         views.SectionDeleteView.as_view(), name='delete_section'),

]
