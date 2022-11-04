
from rest_framework.serializers import ModelSerializer

from my_social_app.models import Tag, Post, Comment, Notification,Chatmessage, ThreadChatMessage, Threads
from my_social_app.models import User, FollowUsers
from rest_framework import serializers
class UserChangeEmailSerializer(ModelSerializer):
    password = serializers.CharField(max_length=225, style={'input_type': 'password'}, write_only=True)
    newEmail = serializers.CharField(max_length=225, style={'input_type': 'newEmail'}, write_only=True)

    class Meta:
        model = User
        fields = ['newEmail', 'password']

    def validate(self, attrs):
        password = attrs.get('password')
        newEmail = attrs.get('newEmail')

        user = self.context.get('user')

        oldEmail = user.email
        print(oldEmail)
        if oldEmail is not None:
            if User.objects.filter(email=newEmail).exists() == False:
                if user.check_password(password) == True:
                    user.email = newEmail
                    user.save()


            else:
                raise serializers.ValidationError('Entered email is already Exists, please enter new one')
        else:
            raise serializers.ValidationError('Your Old Email is not valid')
        return attrs
