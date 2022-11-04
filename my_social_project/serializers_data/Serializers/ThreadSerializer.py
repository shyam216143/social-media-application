from rest_framework.serializers import ModelSerializer

from my_social_app.models import Comment, ThreadChatMessage, Threads, User,FollowUsers
from rest_framework import serializers

from my_social_app.serializers import UserSerializer


class ThreadSerializer(ModelSerializer):
    first_person=UserSerializer()
    second_person=UserSerializer()
    class Meta:
        model =Threads
        fields = '__all__'
