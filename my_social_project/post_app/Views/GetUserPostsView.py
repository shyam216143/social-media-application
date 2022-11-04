from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from my_social_app.models import  Post
from serializers_data.Serializers.GetTimelinePostDataSerializer import GetTimelinePostDataSerializer
from my_social_app.renderers import UserRenderer


class GetUserPostsview(APIView):
    def get(self, request, page=None, size=None):
        lis = []
        current_page = request.GET['page']
        require_size = request.GET['size']
        print(current_page)
        print(require_size)
        i = 1
        largenumber = int(current_page) * int(require_size)
        smaller_number = (int(current_page) - 1) * int(require_size)
        posts = Post.objects.filter(author=request.user)

        for post in posts:
            if (smaller_number - 1) < i < (largenumber + 1):
                timelineposts_serializer = GetTimelinePostDataSerializer(post)
                temp = {
                    "likedByAuthUser": False,
                    "post": timelineposts_serializer.data
                }
                lis.append(temp)
                print(timelineposts_serializer.data, "id is")
            i = 1 + i

        return Response(lis, status=HTTP_200_OK)
