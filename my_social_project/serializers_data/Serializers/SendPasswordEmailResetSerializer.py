
from rest_framework.serializers import ModelSerializer,ValidationError
from my_social_app.models import Tag, Post, Comment, Notification,Chatmessage, ThreadChatMessage, Threads
from my_social_app.models import User, FollowUsers
from rest_framework import serializers
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage, send_mail
from my_social_project.settings import EMAIL_HOST_USER
class SendPasswordEmailResetSerializer(ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        user = self.context.get('user')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("encoded UID", uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("password Reset Token", token)
            link = 'http://localhost:4200/reset-password/' + uid + '/' + token

            print('password Reset Link', link)
            # send email
            body = link

            data = {
                'subject': 'Reset Your password',
                'body': body,
                'to_email': user.email,
            }

            email = EmailMessage(
                subject=data['subject'],
                body=data['body'],
                from_email=EMAIL_HOST_USER,
                to=[data['to_email']]

            )

            email.send()
            return attrs

        else:
            raise ValidationError("Your are a not Registered User")

