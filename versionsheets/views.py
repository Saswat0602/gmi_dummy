from rest_framework import generics
from .models import VersionSheet
from .serializers import VersionSheetSerializer
from rest_framework import permissions

class VersionSheetListCreateView(generics.ListCreateAPIView):
    queryset = VersionSheet.objects.all()
    serializer_class = VersionSheetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VersionSheetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VersionSheet.objects.all()
    serializer_class = VersionSheetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
