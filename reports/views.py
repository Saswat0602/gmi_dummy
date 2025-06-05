from rest_framework import generics
from .models import Report, Sign
from .serializers import ReportSerializer, SignSerializer
from rest_framework import permissions

class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ReportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SignListCreateView(generics.ListCreateAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SignRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sign.objects.all()
    serializer_class = SignSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
