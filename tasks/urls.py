from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, StampListCreateView, StampRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<uuid:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('stamps/', StampListCreateView.as_view(), name='stamp-list-create'),
    path('stamps/<uuid:pk>/', StampRetrieveUpdateDestroyView.as_view(), name='stamp-retrieve-update-destroy'),
]