import pickle

from django.db.models import Q
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from inventory.models import Reservation

from .forms import *
from .models import *



class ProjectsIndexView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'projects/index.html'

class ProjectCreateView(BSModalCreateView):
    template_name = 'projects/create_project.html'
    form_class = ProjectForm
    success_message = 'Success: Project was created'
    success_url =reverse_lazy('projects:index_projects')

class ProjectUpdateView(BSModalUpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = ProjectForm
    success_message = 'Success: Project was updated.'
    success_url = reverse_lazy('projects:index_projects')

class ProjectEditView(generic.DetailView):
    model = Project
    template_name = 'projects/edit_project.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProjectEditView, self).get_context_data(*args, **kwargs)
        project_id = context['project'].id
        # context['reservations'] = Reservation.objects.all()

        project_reservations = ProjectReservation.objects.filter(project__id=project_id)
        context['project_reservations'] = project_reservations

        none_project_reservations = []       
        for reservation in Reservation.objects.all():
            inpr = False
            for project_reservation in project_reservations:
                if project_reservation.reservation.id == reservation.id:
                    inpr = True
            if inpr == False:
                none_project_reservations.append(reservation)

        context['none_project_reservations'] = none_project_reservations

        return context

class ProjectReadView(BSModalReadView):
    model = Project
    template_name = 'projects/read_project.html'

class ProjectDeleteView(BSModalDeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    success_message = 'Success: Projects was deleted'
    success_url = reverse_lazy('projects:index_projects')

def clear_project_reservations(request):
    project_id = request.POST.get('project_id')
    project_obj = Project.objects.get(id=project_id)
    project_reservations = ProjectReservation.objects.filter(project=project_obj).delete()

    return redirect("/projects/edit/{project_id}".format(project_id=project_id))

def add_project_reservation(request):
    project_id = request.POST.get('project_id')
    none_project_reservations = request.POST.get('none_project_reservations')

    return redirect("/projects/edit/{project_id}".format(project_id=project_id))

def add_reservations(request):
    project_id = request.POST.get('project_id')
    project_obj = Project.objects.get(id=project_id)

    checked_items = request.POST.get('checked_items')
    # TODO: Split string and add reservations to project
    sci = checked_items.split(";")
    ici = [int(s) for s in sci]
    for reservation_id in ici:
        reservation_obj = Reservation.objects.get(id=reservation_id)
        ProjectReservation.objects.get_or_create(reservation=reservation_obj, project=project_obj)

    return redirect("/projects/edit/{project_id}".format(project_id=project_id))


def delete_project_reservation(request):
    project_id = request.POST.get('project_id')
    reservation_id = request.POST.get('reservation_id')
    project_obj = Project.objects.get(id=project_id)
    project_reservation = ProjectReservation.objects.filter(id=reservation_id, project=project_obj).delete()
    
    return redirect("/projects/edit/{project_id}".format(project_id=project_id))
