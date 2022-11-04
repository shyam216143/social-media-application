from rest_framework.serializers import ModelSerializer

from my_social_app.models import User,FollowUsers, Post
from rest_framework import serializers
from serializers_data.Serializers.PostSerializer import PostSerializer
from serializers_data.Serializers.TagSerializer import TagSerializer

from serializers_data.Serializers.UserLoginSerializer import LoginDataSerializer
from serializers_data.Serializers.GetPostDataByIdSerializer import GetPostDataByIdSerializer


class GetTimelinePostDataSerializer(ModelSerializer):
    author = LoginDataSerializer()
    postTags = TagSerializer(many=True)
    sharedPost=PostSerializer()

    class Meta:
        model = Post
        fields = "__all__"