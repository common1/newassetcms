from django.contrib import admin

from .models import (
    Project,
    ProjectReservation,
)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'manager', 'start_date', 'end_date', 'active']
admin.site.register(Project, ProjectAdmin)

class ProjectReservationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'reservation', 'project', 'active']
admin.site.register(ProjectReservation, ProjectReservationAdmin)
