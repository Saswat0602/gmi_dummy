from django.urls import path
from .views import DocumentListCreateView, DocumentRetrieveUpdateDestroyView

urlpatterns = [
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('documents/<uuid:pk>/', DocumentRetrieveUpdateDestroyView.as_view(), name='document-retrieve-update-destroy'),
]