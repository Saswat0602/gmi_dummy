from django.db import models
import uuid
from django.conf import settings
from sheets.models import Sheet
from projects.models import Project

class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photos')
    sheets = models.ManyToManyField(Sheet, related_name='photos', blank=True)
    
    url = models.URLField()
    raw_url = models.URLField()
    default_url = models.URLField()
    large_url = models.URLField()
    thumbnail_url = models.URLField()
    
    title = models.CharField(max_length=255, blank=True, null=True)
    tags = models.JSONField(blank=True, null=True)
    tmp_uri = models.CharField(max_length=500, blank=True, null=True)
    filename = models.CharField(max_length=255)
    
    modified_at = models.DateTimeField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_temporarily_present = models.BooleanField(default=False)
    is_annotation = models.BooleanField(default=False)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='uploaded_photos')

class PhotoAnnotation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photoannotations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='photoannotations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='photo_annotations')
    published = models.BooleanField(default=False)
    type = models.CharField(max_length=100)
    shape_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
