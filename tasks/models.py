from django.db import models
import uuid
from django.conf import settings
from projects.models import Project
from sheets.models import Sheet
from photos.models import Photo
# Remove: from reports.models import Report

class Stamp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='stamps')
    name = models.CharField(max_length=255)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    
    sheet = models.ForeignKey(Sheet, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    report = models.ForeignKey('reports.Report', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')  # Use string here
    photos = models.ManyToManyField(Photo, related_name='tasks', blank=True)
    stamp = models.ForeignKey(Stamp, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    
    type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    list_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100)
    task_num = models.IntegerField()

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    root_cause_id = models.UUIDField(null=True, blank=True)
    list_attributes = models.JSONField(blank=True, null=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_tasks')
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned_tasks', blank=True)
    watching = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watched_tasks', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
