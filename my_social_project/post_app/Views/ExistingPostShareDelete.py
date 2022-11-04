import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import Tag, Post, PostLike, Comment, CommentLikes, User
from my_social_app.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated


class ExistingPostShareDelete(APIView):
    def post(self, request, post_id):
        post_id = post_id
        print(post_id)
        post_data = Post.objects.get(id=post_id)
        post_likes = PostLike.objects.select_related('post').filter(post=post_data)
        for post_like in post_likes:
            post_like.delete()
        comments_data = Comment.objects.select_related('post').filter(post=post_data)
        for comment_data in comments_data:

            comment_likes = CommentLikes.objects.select_related('comment').filter(comment=comment_data)
            for comment_like in comment_likes:
                comment_like.delete()
            comments_data.delete()
        post_data.delete()
        return Response({"msg": "Successfully Deleted"}, status=HTTP_200_OK)
