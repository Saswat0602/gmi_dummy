from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi

class TestView(APIView):
    def get(self, request):
        generator = OpenAPISchemaGenerator(info=openapi.Info(title="Test API", version="1.0.0", default_version="1.0"))
        return Response({"message": "Test successful"})