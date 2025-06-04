from django.db import models
import uuid
from projects.models import Project
from django.utils import timezone

class VersionSheet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='version_sheets')
    name = models.CharField(max_length=255)
    issuance_date = models.DateField(null=True, blank=True, default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def formatted_issuance_date(self):
        if self.issuance_date:
            return self.issuance_date.strftime('%Y-%m-%d')
        return None
