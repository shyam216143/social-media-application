import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Tag, Post
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..models import FollowUsers, User
from ..serializers import PostSerializer, TagSerializer


class CreatePostView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content = request.data['content']
        postPhoto = request.data['postPhoto']
        postTags = request.data['postTags']
        user=request.user
        print(user)
        create_post= Post(post_photo=postPhoto,content=content,).save()
        print(content)
        print(postPhoto)
        postTags= json.loads(postTags)
        for i in postTags:
            print(i["tagName"])
        print(postTags)

        return Response({"msg":"success"}, status=HTTP_200_OK)
