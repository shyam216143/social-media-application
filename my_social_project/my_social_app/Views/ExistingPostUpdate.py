import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Tag, Post
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..models import FollowUsers, User
from ..serializers import PostSerializer, TagSerializer, GetPostDataByIdSerializer


class ExistingPostUpdate(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id=None):
        update_post = Post.objects.get(id=post_id)
        content = request.data['content']
        postPhoto = request.data['postPhoto']
        postTags = request.data['postTags']
        update_post.content = content
        update_post.postPhoto = postPhoto
        update_post.save()
        postTags = json.loads(postTags)
        for tag in postTags:

            if tag['action'] == 'add':
                create_tag = Tag(name=tag['tagName'])
                create_tag.tagUseCounter = 1
                create_tag.save()
                update_post.postTags.set(create_tag)
                update_post.save()

            else:
                update_tag = Tag.objects.get(name=tag['tagName'])
                update_tag.tagUseCounter = update_tag.tagUseCounter - 1
                update_post.postTags.set('')
                update_tag.save()


                print(update_post)
                print(update_tag)
        serializer = GetPostDataByIdSerializer(update_post)
        return Response(serializer.data, status=HTTP_200_OK)


        #     tag_exists = Tag.objects.filter(name=tag['tagName']).exists()
        #     if not tag_exists:
        #         create_tag = Tag(name=tag['tagName'])
        #         create_tag.tagUseCounter = 1
        #         create_tag.save()
        #         update_post.postTags = postTags
        #         update_post.save()
        #     else:
        #         if tag['action'] == 'add':
        #             update_tag = Tag.objects.get(name=tag['tagName'])
        #             print(update_tag)
        #             update_tag.tagUseCounter = update_tag.tagUseCounter + 1
        #             update_tag.save()
        #             update_post.save()
        #             print(update_post)
        #             print(update_tag)
        #         else:
        #             update_tag = Tag.objects.get(name=tag['tagName'])
        #             update_tag.tagUseCounter = update_tag.tagUseCounter - 1
        #             update_post.postTags.set('')
        #             update_tag.save()
        #
        #             print(update_post)
        #             print(update_tag)
        # serializer = GetPostDataByIdSerializer(update_post)
        # return Response(serializer.data, status=HTTP_200_OK)
