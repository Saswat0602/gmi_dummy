from django.db import models
import uuid
from django.conf import settings
from projects.models import Project
from versionsheets.models import VersionSheet

class Sheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sheets')
    version_sheet = models.ForeignKey(VersionSheet, on_delete=models.CASCADE, related_name='sheets')
    dpi = models.CharField(max_length=10)
    num = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    tags = models.JSONField(blank=True, null=True)
    width = models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    pdf_url = models.URLField()
    page_index = models.IntegerField(default=0)
    plan_set_id = models.UUIDField()
    full_img_url = models.URLField()
    version_set_id = models.UUIDField()
    plan_set_s3_url = models.URLField()
    thumbnail_url = models.URLField()
    plan_set_filename = models.CharField(max_length=255)
    text_extract_data_url = models.URLField()
    text_detect_full_page_url = models.URLField()

    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='uploaded_sheets')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SheetAnnotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE, related_name='sheetannotations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='sheetannotations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='sheet_annotations')
    published = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    shape_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
