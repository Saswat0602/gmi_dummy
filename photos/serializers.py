from rest_framework import serializers
from .models import Photo, PhotoAnnotation

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'project', 'sheets', 'url', 'raw_url', 'default_url', 'large_url', 'thumbnail_url', 'title', 'tags', 'tmp_uri', 'filename', 'modified_at', 'uploaded_at', 'is_temporarily_present', 'is_annotation', 'uploaded_by')
        depth = 1

class PhotoAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoAnnotation
        fields = ('id', 'photo', 'project', 'user', 'published', 'type', 'shape_data', 'created_at', 'updated_at')