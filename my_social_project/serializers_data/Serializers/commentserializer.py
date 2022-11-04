
from rest_framework.serializers import ModelSerializer

from my_social_app.models import Comment, User,FollowUsers
from rest_framework import serializers

from serializers_data.Serializers.UsersSerializer import UserSerializer

class commentserializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        exclude = ('post',)
