
from rest_framework.serializers import ModelSerializer

from my_social_app.models import User, Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

