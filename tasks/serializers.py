from rest_framework import serializers
from .models import Task, Stamp

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'type', 'title', 'list_id', 'status', 'task_num', 'start_date', 'end_date', 'description', 'root_cause_id', 'list_attributes', 'created_at', 'updated_at')
        depth = 1

class StampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stamp
        fields = ('id', 'name', 'image_url', 'created_at')