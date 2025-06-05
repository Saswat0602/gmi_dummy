from rest_framework import serializers
from .models import VersionSheet

class VersionSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionSheet
        fields = ('id', 'project', 'name', 'issuance_date', 'created_at', 'updated_at')
        depth = 1