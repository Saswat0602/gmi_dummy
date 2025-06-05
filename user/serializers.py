from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fullname', 'first_name', 'last_name', 'email', 'username', 'phone', 'is_active', 'is_superuser', 'date_joined', 'last_login', 'profile_picture', 'bio', 'role', 'region_ids', 'is_verified')
        depth = 0