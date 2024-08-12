import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import Tag, Post
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..models import User
from ..serializers import PostSerializer


class CreatePostView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        content = request.data['content']
        postPhoto = request.data['postPhoto']
        postTags = request.data['postTags']
        user = request.user
        user1 = User.objects.filter(id=user.id).first()
        create_post = Post(postPhoto=postPhoto, content=content, author=user1)

        create_post.save()
        postTags = json.loads(postTags)
        for i in postTags:
            tag = Tag.objects.filter(name=i["tagName"]).exists()
            if not tag:
                create_tag = Tag(name=i["tagName"])
                create_tag.tagUseCounter = 1
                create_tag.save()
            else:
                update_tag = Tag.objects.get(name=i["tagName"])
                update_tag.tagUseCounter = update_tag.tagUseCounter + 1
                update_tag.save()
            post_tag = Tag.objects.get(name=i["tagName"])
            create_post.postTags.add(post_tag.id)
            serializer = PostSerializer(create_post)
            create_post.save()

        return Response(serializer.data, status=HTTP_200_OK)
