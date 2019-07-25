from django.urls import path

from . import views


urlpatterns = [
    path('samples/', views.Index.as_view(), name='index'),
]
