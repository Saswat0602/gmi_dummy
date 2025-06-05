from rest_framework import serializers
from .models import Report, Sign

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ('id', 'name', 'template_id', 'status', 'data', 'published', 'created_by', 'updated_by', 'created_at', 'updated_at')
        depth = 0

class SignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sign
        fields = ('id', 'Key', 'rawUrl', 'thumbnailUrl', 'name', 'file_url', 'created_at')