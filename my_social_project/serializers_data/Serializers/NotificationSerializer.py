

from rest_framework.serializers import ModelSerializer

from my_social_app.models import Notification, User, Post
from rest_framework import serializers
from serializers_data.Serializers.GetPostDataByIdSerializer import GetPostDataByIdSerializer

from serializers_data.Serializers.UsersSerializer import UserSerializer
from serializers_data.Serializers.commentserializer import commentserializer


class NotificationSerializer(ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()
    owningComment = commentserializer()
    owningPost = GetPostDataByIdSerializer()

    class Meta:
        model = Notification
        fields = '__all__'