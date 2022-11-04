
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User,FollowUsers
from rest_framework import serializers

class FollowUsersSerializer(ModelSerializer):
    class Meta:
        model = FollowUsers
        fields = ['follower', 'followed', ]




class FollowerDataSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ('password', 'last_login', 'date_joined', 'date_last_modified', 'join_date', 'is_admin', 'is_staff',
                   'is_superuser', 'is_active', 'groups', 'user_permissions', 'created_at', 'updated_at')

