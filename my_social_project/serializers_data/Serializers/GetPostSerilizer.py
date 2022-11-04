
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User, Post
from rest_framework import serializers
from my_social_app.serializers import PostSerializer

from serializers_data.Serializers.TagSerializer import TagSerializer
from serializers_data.Serializers.UserLoginSerializer import LoginDataSerializer

class GetPostSerilizer(ModelSerializer):
    author = LoginDataSerializer()
    postTags = TagSerializer(many=True)
    sharedPost=PostSerializer()

    class Meta:
        model = Post
        fields = "__all__"