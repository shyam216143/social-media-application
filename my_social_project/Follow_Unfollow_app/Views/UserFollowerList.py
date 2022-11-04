from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import FollowUsers, User
from serializers_data.Serializers.FollowusersSerializer import FollowUsersSerializer, FollowerDataSerializer
from my_social_app.renderers import UserRenderer


class UserFollowerListView(APIView):
    def get(self, request,id=None,page=None, size=None):
        follower_data = FollowUsers.objects.filter(followed=id)
        print(follower_data)
        lis = []
        current_page = request.GET['page']
        require_size = request.GET['size']
        print(current_page)
        print(require_size)
        i = 1
        largenumber = int(current_page) * int(require_size)
        smaller_number = (int(current_page) - 1) * int(require_size)

        for following in follower_data:
            if (smaller_number - 1) < i < (largenumber + 1):
                user = User.objects.get(id=following.follower.id)
                followedByuser = FollowUsers.objects.filter(follower=request.user.id,
                                                            followed=following.followed.id).exists()
                print(followedByuser)
                following_serializer = FollowerDataSerializer(user)

                temp = {
                    "user": following_serializer.data,
                    "followedByAuthUser": followedByuser

                }
                print(followedByuser)
                lis.append(temp)
            i=1+i

        return Response({"msg": "Success", "list": lis})

