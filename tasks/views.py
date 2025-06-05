from rest_framework import generics
from .models import Task, Stamp
from .serializers import TaskSerializer, StampSerializer
from rest_framework import permissions

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StampListCreateView(generics.ListCreateAPIView):
    queryset = Stamp.objects.all()
    serializer_class = StampSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StampRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stamp.objects.all()
    serializer_class = StampSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
