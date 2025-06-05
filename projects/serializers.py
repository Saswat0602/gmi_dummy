from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'num', 'start_date', 'updated_at', 'created_at', 'status', 'regions', 'address', 'officers', 'last_task_num')
        depth = 0