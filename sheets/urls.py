from django.urls import path
from .views import SheetListCreateView, SheetRetrieveUpdateDestroyView, SheetAnnotationListCreateView, SheetAnnotationRetrieveUpdateDestroyView

urlpatterns = [
    path('sheets/', SheetListCreateView.as_view(), name='sheet-list-create'),
    path('sheets/<uuid:pk>/', SheetRetrieveUpdateDestroyView.as_view(), name='sheet-retrieve-update-destroy'),
    path('sheetannotations/', SheetAnnotationListCreateView.as_view(), name='sheetannotation-list-create'),
    path('sheetannotations/<uuid:pk>/', SheetAnnotationRetrieveUpdateDestroyView.as_view(), name='sheetannotation-retrieve-update-destroy'),
]