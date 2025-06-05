from rest_framework import generics
from .models import Sheet, SheetAnnotation
from .serializers import SheetSerializer, SheetAnnotationSerializer
from rest_framework import permissions

class SheetListCreateView(generics.ListCreateAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SheetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SheetAnnotationListCreateView(generics.ListCreateAPIView):
    queryset = SheetAnnotation.objects.all()
    serializer_class = SheetAnnotationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SheetAnnotationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SheetAnnotation.objects.all()
    serializer_class = SheetAnnotationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
