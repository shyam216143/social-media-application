
from rest_framework.serializers import ModelSerializer

from my_social_app.models import Tag, Post, Comment, Notification,Chatmessage, ThreadChatMessage, Threads
from my_social_app.models import User, FollowUsers
from rest_framework import serializers
class UserRegisterationsSerializer(ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    print("hello")

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'username', 'first_name', 'last_name', ]
        extra_kwargs = {
            'password': {'write_only': True, }
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirmed Password not matched")
        return attrs
      
    def create(self, validate_date):
        print(validate_date, "validate data")
        return User.objects.create_user(**validate_date)