import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import Tag, Post, PostLike, Comment, CommentLikes, User
from my_social_app.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated



class PostCommentDeleteView(APIView):
    def post(self, request, post_id=None, commentId=None):
        post_data = Post.objects.get(id=post_id)
        comment_data = Comment.objects.get(id=commentId)
        post_data.commentCount = post_data.commentCount - 1
        post_data.save()
        comment_likes = CommentLikes.objects.filter(comment=comment_data)
        for comment_like in comment_likes:
            comment_like.delete()
        comment_data.delete()
        return Response({'msg': "Success"}, status=HTTP_200_OK)
