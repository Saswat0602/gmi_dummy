from django.db import models
import uuid
from projects.models import Project
from photos.models import Photo
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reports')

    name = models.CharField(max_length=255)
    template_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')

    data = models.JSONField(default=dict, blank=True)
    photos = models.ManyToManyField(Photo, related_name='reports', blank=True)

    published = models.BooleanField(default=False)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_reports')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='updated_reports')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.status})"


class Sign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='signatures')

    name = models.CharField(max_length=255)
    file_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def project(self):
        return self.report.project

    def __str__(self):
        return f"Sign by {self.name}"
