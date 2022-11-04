
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User
from rest_framework import serializers

class ProfilePhotoSerializer(ModelSerializer):
    # profile_photo = serializers.ImageField(max_length=225, style={'input_type': 'profilePhoto'}, write_only=True)
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('password', 'last_login', 'date_joined', 'date_last_modified', 'join_date', 'is_admin', 'is_staff',
                   'is_superuser', 'is_active', 'groups', 'user_permissions', 'created_at', 'updated_at')
