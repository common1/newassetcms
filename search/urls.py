from django.urls import path

from .views import (
    SearchAssetsIndexView,
)

app_name = 'search'
urlpatterns = [
    path('', SearchAssetsIndexView.as_view(), name='query'),
]
