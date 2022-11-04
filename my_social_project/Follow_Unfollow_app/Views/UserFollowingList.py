from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.models import FollowUsers, User
from serializers_data.Serializers.FollowusersSerializer import FollowUsersSerializer, FollowerDataSerializer
from my_social_app.renderers import UserRenderer


class UserFollowingListView(APIView):
    def get(self, request,id=None,page=None, size=None):
        
        lis = []
        current_page = request.GET['page']
        require_size = request.GET['size']
        
        following_data = FollowUsers.objects.filter(follower=id)
        print(following_data)
      
        i = 1
        print(i)
        largenumber = int(current_page) * int(require_size)
        smaller_number = (int(current_page) - 1) * int(require_size)
        print(largenumber)
        print(smaller_number)
        for following in following_data:
            if (smaller_number ) < i < (largenumber + 1):
                user = User.objects.get(id=following.followed.id)
                followedByuser = FollowUsers.objects.filter(follower=request.user.id,
                                                            followed=following.followed.id).exists()
                following_serializer = FollowerDataSerializer(user)
                
                temp = {
                    "user": following_serializer.data,
                    "followedByAuthUser": followedByuser

                }
                print(following_serializer.data)
                lis.append(temp)
            i=1+i
        print(lis)

        return Response({"msg": "Success", "list": lis})
