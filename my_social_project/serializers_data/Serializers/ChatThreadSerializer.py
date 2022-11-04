
from rest_framework.serializers import ModelSerializer

from my_social_app.models import Comment, ThreadChatMessage, User,FollowUsers
from rest_framework import serializers

from my_social_app.serializers import ThreadSerializer, UserSerializer

class ChatThreadSerializer(ModelSerializer):
    thread=ThreadSerializer()
    user=UserSerializer()
    class Meta:
        model =ThreadChatMessage
        fields='__all__'

