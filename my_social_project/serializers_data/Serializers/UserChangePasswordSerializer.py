

from rest_framework.serializers import ModelSerializer

from my_social_app.models import Tag, Post, Comment, Notification,Chatmessage, ThreadChatMessage, Threads
from my_social_app.models import User, FollowUsers
from rest_framework import serializers
class UserChangePasswordSerializer(ModelSerializer):
    password = serializers.CharField(max_length=225, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=225, style={'input_type': 'password2'}, write_only=True)
    oldpassword = serializers.CharField(max_length=225, style={'input_type': 'oldpassword'}, write_only=True)

    class Meta:
        model = User
        fields = ['password', 'password2', 'oldpassword']

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        oldpassword = attrs.get('oldpassword')

        user = self.context.get('user')

        print(user.check_password(oldpassword))

        if user.check_password(oldpassword) == False:
            raise serializers.ValidationError(
                "old password is not matched with existing password, enter correct existing password")

        if password != password2:
            raise serializers.ValidationError("password and confirmed Password not matched")
        user.set_password(password)
        user.save()
        return attrs