from django.conf.urls import url
from django.urls import path

from .views import (
    SearchAssetView,
)

app_name = 'search'
urlpatterns = [
    path('', SearchAssetView.as_view(), name='query'),
]
