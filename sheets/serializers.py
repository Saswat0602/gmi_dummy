from rest_framework import serializers
from .models import Sheet, SheetAnnotation

class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = ('id', 'project', 'version_sheet', 'dpi', 'num', 'name', 'tags', 'width', 'height', 'pdf_url', 'page_index', 'plan_set_id', 'full_img_url', 'version_set_id', 'plan_set_s3_url', 'thumbnail_url', 'plan_set_filename', 'text_extract_data_url', 'text_detect_full_page_url', 'uploaded_by', 'created_at', 'updated_at')
        depth = 1

class SheetAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SheetAnnotation
        fields = ('id', 'sheet', 'project', 'user', 'published', 'type', 'shape_data', 'created_at', 'updated_at')