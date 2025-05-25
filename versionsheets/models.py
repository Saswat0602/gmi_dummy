from django.db import models
import uuid
from projects.models import Project

class VersionSheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='version_sheets')
    name = models.CharField(max_length=255)
    issuance_date = models.DateField()
    formatted_issuance_date = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
