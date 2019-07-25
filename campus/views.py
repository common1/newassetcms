from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

from .forms import (
    FacultyForm,
    BuildingForm,
    LocationForm,
    SectionForm,
)
from .models import (
    Faculty,
    Building,
    Location,
    Section,
)

# Faculty


class FacultiesIndexView(generic.ListView):
    model = Faculty
    context_object_name = 'faculties'
    template_name = 'campus/faculties/index.html'


class FacultyCreateView(BSModalCreateView):
    template_name = 'campus/faculties/create_faculty.html'
    form_class = FacultyForm
    success_message = 'Success: Faculty was created.'
    success_url = reverse_lazy('campus:index_faculties')


class FacultyUpdateView(BSModalUpdateView):
    model = Faculty
    template_name = 'campus/faculties/update_faculty.html'
    form_class = FacultyForm
    success_message = 'Success: Faculty was updated.'
    success_url = reverse_lazy('campus:index_faculties')


class FacultyReadView(BSModalReadView):
    model = Faculty
    template_name = 'campus/faculties/read_faculty.html'


class FacultyDeleteView(BSModalDeleteView):
    model = Faculty
    template_name = 'campus/faculties/delete_faculty.html'
    success_message = 'Success: Faculty was deleted.'
    success_url = reverse_lazy('campus:index_faculties')

# Building


class BuildingsIndexView(generic.ListView):
    model = Building
    context_object_name = 'buildings'
    template_name = 'campus/buildings/index.html'


class BuildingCreateView(BSModalCreateView):
    template_name = 'campus/buildings/create_building.html'
    form_class = BuildingForm
    success_message = 'Success: Building was created.'
    success_url = reverse_lazy('campus:index_buildings')


class BuildingUpdateView(BSModalUpdateView):
    model = Building
    template_name = 'campus/buildings/update_building.html'
    form_class = BuildingForm
    success_message = 'Success: Building was updated.'
    success_url = reverse_lazy('campus:index_buildings')


class BuildingReadView(BSModalReadView):
    model = Building
    template_name = 'campus/buildings/read_building.html'


class BuildingDeleteView(BSModalDeleteView):
    model = Building
    template_name = 'campus/buildings/delete_building.html'
    success_message = 'Success: Building was deleted.'
    success_url = reverse_lazy('campus:index_buildings')

# Location


class LocationsIndexView(generic.ListView):
    model = Location
    context_object_name = 'locations'
    template_name = 'campus/locations/index.html'


class LocationCreateView(BSModalCreateView):
    template_name = 'campus/locations/create_location.html'
    form_class = LocationForm
    success_message = 'Success: Location was created.'
    success_url = reverse_lazy('campus:index_locations')


class LocationUpdateView(BSModalUpdateView):
    model = Location
    template_name = 'campus/locations/update_location.html'
    form_class = LocationForm
    success_message = 'Success: Location was updated.'
    success_url = reverse_lazy('campus:index_locations')


class LocationReadView(BSModalReadView):
    model = Location
    template_name = 'campus/locations/read_location.html'


class LocationDeleteView(BSModalDeleteView):
    model = Location
    template_name = 'campus/locations/delete_location.html'
    success_message = 'Success: Location was deleted.'
    success_url = reverse_lazy('campus:index_locations')

# Section


class SectionsIndexView(generic.ListView):
    model = Section
    context_object_name = 'sections'
    template_name = 'campus/sections/index.html'


class SectionCreateView(BSModalCreateView):
    template_name = 'campus/sections/create_section.html'
    form_class = SectionForm
    success_message = 'Success: Section was created.'
    success_url = reverse_lazy('campus:index_sections')


class SectionUpdateView(BSModalUpdateView):
    model = Section
    template_name = 'campus/sections/update_section.html'
    form_class = SectionForm
    success_message = 'Success: Section was updated.'
    success_url = reverse_lazy('campus:index_sections')


class  SectionReadView(BSModalReadView):
    model =  Section
    template_name = 'campus/sections/read_section.html'


class SectionDeleteView(BSModalDeleteView):
    model = Section
    template_name = 'campus/sections/delete_section.html'
    success_message = 'Success: Section was deleted.'
    success_url = reverse_lazy('campus:index_sections')
