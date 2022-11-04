


import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import Tag, Post, PostLike, Comment, FollowUsers, Notification
from my_social_app.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from serializers_data.Serializers.NotificationSerializer import NotificationSerializer


class NotificationMarkAllSeenView(APIView):
    def post(self, request):
        set_notifications_seen = Notification.objects.filter(receiver=request.user, isSeen=False)
        for set_notification_seen in set_notifications_seen:
            set_notification_seen.isSeen=True
            set_notification_seen.save()

        print(set_notifications_seen, "notifications is")
        return Response({"msg":"success"}, status=HTTP_200_OK)
