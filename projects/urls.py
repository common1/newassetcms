from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
    path('projects/',
         views.ProjectsIndexView.as_view(), name='index_projects'),
    path('projects/create/',
         views.ProjectCreateView.as_view(), name='create_project'),
    path('projects/update/<int:pk>',
         views.ProjectUpdateView.as_view(), name='update_project'),
    path('projects/edit/<int:pk>',
         views.ProjectEditView.as_view(), name='edit_project'),
    path('projects/read/<int:pk>',
         views.ProjectReadView.as_view(), name='read_project'),
    path('projects/delete/<int:pk>',
         views.ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/clearprojectreservations/',
         views.clear_project_reservations, name='clear_project_reservations'),
    path('projects/addprojectreservation/<int:pk>',
         views.add_project_reservation, name='add_project_reservation'),
    path('projects/addreservations/',
         views.add_reservations, name='add_reservations'),
    path('projects/deletereservation/',
         views.delete_project_reservation, name='delete_project_reservation'),


]

