from rest_framework import generics
from .models import Photo, PhotoAnnotation
from .serializers import PhotoSerializer, PhotoAnnotationSerializer
from rest_framework import permissions

class PhotoListCreateView(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhotoAnnotationListCreateView(generics.ListCreateAPIView):
    queryset = PhotoAnnotation.objects.all()
    serializer_class = PhotoAnnotationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PhotoAnnotationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhotoAnnotation.objects.all()
    serializer_class = PhotoAnnotationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
