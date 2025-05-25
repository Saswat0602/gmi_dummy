from django.db import models
import uuid
from projects.models import Project

class Document(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
    file_url = models.URLField()
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
