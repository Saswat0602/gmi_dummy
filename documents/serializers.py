from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'project', 's3Url', 'file_url', 'name', 'dirPath', 'description', 'filename', 'file_type', 'file_size', 'uploaded_at')
        depth = 1