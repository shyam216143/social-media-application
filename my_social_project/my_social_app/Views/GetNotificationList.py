import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Tag, Post, PostLike, Comment, FollowUsers, Notification
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..serializers import NotificationSerializer


class GetNotification(APIView):
    def get(self, request):
        get_notifications = Notification.objects.filter(receiver=request.user, isRead=False, isSeen=False)
        print(get_notifications, "notifications is")
        lis = []
        for get_notification in get_notifications:
            serializer = NotificationSerializer(get_notification)
            lis.append(serializer.data)
        return Response(lis, status=HTTP_200_OK)
