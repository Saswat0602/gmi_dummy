from django.urls import path
from .views import PhotoListCreateView, PhotoRetrieveUpdateDestroyView, PhotoAnnotationListCreateView, PhotoAnnotationRetrieveUpdateDestroyView

urlpatterns = [
    path('photos/', PhotoListCreateView.as_view(), name='photo-list-create'),
    path('photos/<uuid:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo-retrieve-update-destroy'),
    path('photoannotations/', PhotoAnnotationListCreateView.as_view(), name='photoannotation-list-create'),
    path('photoannotations/<uuid:pk>/', PhotoAnnotationRetrieveUpdateDestroyView.as_view(), name='photoannotation-retrieve-update-destroy'),
]