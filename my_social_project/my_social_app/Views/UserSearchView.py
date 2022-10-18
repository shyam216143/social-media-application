import json
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from my_social_app.serializers import UserSerializer

from ..models import FollowUsers, User


class UserSearchView(APIView):
    def get(self, request):
        current_user= request.user
        current_page = request.GET['page']
        require_size = request.GET['size']
        key = request.GET['key']
        lis=[]
        users = User.objects.filter(username__contains=str(key) )|User.objects.filter(email__contains=str(key))|User.objects.filter(first_name__contains=str(key) )|User.objects.filter(last_name__contains=str(key) )
        print(users)
        i=1
        if users is not None:
            for user in users:
                if int(current_page) - 1 < i < int(require_size) + 1:
                    print(current_user,"current user")
                    print(user,"display user")
                    if user !=current_user:

                        followedByAuthUser=FollowUsers.objects.filter(follower=current_user, followed=user).exists()
                        print(followedByAuthUser,"is following")
                        serializer=UserSerializer(user)
                        print(serializer.data)
                        temp={
                            "user":serializer.data,
                            "followedByAuthUser":followedByAuthUser

                        }
                        lis.append(temp)
                i=i+1    
            # print(lis)
            return Response(lis, status=HTTP_200_OK)
        return Response('error occered',status=HTTP_400_BAD_REQUEST)    

