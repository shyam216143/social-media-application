
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User, Post
from rest_framework import serializers
from serializers_data.Serializers.GetPostSerilizer import GetPostSerilizer
from serializers_data.Serializers.TagSerializer import TagSerializer

from serializers_data.Serializers.UserLoginSerializer import LoginDataSerializer


class GetPostDataByIdSerializer(ModelSerializer):
    author = LoginDataSerializer()
    postTags = TagSerializer(many=True)
    sharedPost=GetPostSerilizer()
    class Meta:
        model = Post
        fields = "__all__"