from django.db import models
import uuid
from projects.models import Project

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    s3Url = models.URLField(blank=True, null=True, default='')
    file_url = models.URLField(blank=True, null=True, default='')
    name = models.CharField(max_length=255)
    dirPath = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=50, blank=True, null=True)
    file_size = models.PositiveIntegerField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
