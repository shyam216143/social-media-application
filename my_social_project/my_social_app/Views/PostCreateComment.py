import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Tag, Post, PostLike, Comment
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..serializers import commentserializer


class PostCreateCommentView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id=None):
        print(post_id)
        post_data = Post.objects.get(id=post_id)
        print("post data is:", post_data)
        current_user = request.user
        print("current user is", current_user)
        content = request.data['content']
        print(content)
        likedbyUser = PostLike.objects.filter(post=post_data, liker=request.user).exists()
        print(likedbyUser)
        post_comment = Comment(content=content, author=current_user, post=post_data)
        post_comment.save()
        post_data.commentCount=post_data.commentCount+1
        post_data.save()
        print("post content is ",post_comment)

        serializer = commentserializer(post_comment)
        print(serializer.data)
        temp = {
            "likedByAuthUser": likedbyUser,
            "comment": serializer.data

        }

        return Response(temp, status=HTTP_200_OK)
