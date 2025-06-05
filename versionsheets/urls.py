from django.urls import path
from .views import VersionSheetListCreateView, VersionSheetRetrieveUpdateDestroyView

urlpatterns = [
    path('versionsheets/', VersionSheetListCreateView.as_view(), name='versionsheet-list-create'),
    path('versionsheets/<uuid:pk>/', VersionSheetRetrieveUpdateDestroyView.as_view(), name='versionsheet-retrieve-update-destroy'),
]