from django.db import models
import uuid
from reports.models import Report

class Sign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='signs')

    name = models.CharField(max_length=255)
    file_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def project(self):
        return self.report.project

    def __str__(self):
        return f"Sign by {self.name}"
