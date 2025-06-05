from django.urls import path
from .views import ReportListCreateView, ReportRetrieveUpdateDestroyView, SignListCreateView, SignRetrieveUpdateDestroyView

urlpatterns = [
    path('reports/', ReportListCreateView.as_view(), name='report-list-create'),
    path('reports/<uuid:pk>/', ReportRetrieveUpdateDestroyView.as_view(), name='report-retrieve-update-destroy'),
    path('signs/', SignListCreateView.as_view(), name='sign-list-create'),
    path('signs/<uuid:pk>/', SignRetrieveUpdateDestroyView.as_view(), name='sign-retrieve-update-destroy'),
]