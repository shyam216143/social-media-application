
from rest_framework.serializers import ModelSerializer

from my_social_app.models import Tag, Post, Comment, Notification,Chatmessage, ThreadChatMessage, Threads
from my_social_app.models import User, FollowUsers
from rest_framework import serializers
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", 'username', 'first_name', 'last_name', 'intro', 'hometown', 'current_city',
                  'workplace',
                  'edu_institution', 'profile_photo', 'cover_photo', 'role', 'follower_count', 'following_count',
                  'birth_date', 'gender', "country", 'enabled', 'account_verified', 'email_verified', 'join_date']
