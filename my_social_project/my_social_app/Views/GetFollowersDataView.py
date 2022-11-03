import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import  FollowUsers, ThreadChatMessage, Threads,User
from ..renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated

from ..serializers import ChatThreadSerializer, NotificationSerializer, UserSerializer


class GetFollowersData(APIView):
    def get(self, request, user_id=None):
        user = User.objects.get(id=user_id)
        print(user)
        users_followers = FollowUsers.objects.filter(followed=user)
        print("usre followers is",users_followers)
        users_following = FollowUsers.objects.filter(follower=user)
        print("usre followeing is",users_following)

        lis=[]
        for users_following in users_following:
            print(users_following)
            user_following_data= User.objects.get(id=users_following.followed.id)
            print(user_following_data)
            serializer= UserSerializer(user_following_data)
            # 
            current_user= user
            target_chat_user = user_following_data
            print("hjjjhjh",target_chat_user)
            print(current_user)
            lis1=[]
            threads= Threads.objects.filter(first_person=current_user,second_person=target_chat_user)|Threads.objects.filter(first_person=target_chat_user,second_person=current_user)
            if threads.exists():
                chatmessages=ThreadChatMessage.objects.filter(thread=threads.first()).order_by('timestamp')
                for chat_message in chatmessages:
                    serialize= ChatThreadSerializer(chat_message)
                    lis1.append(serialize.data)
            length=len(lis1)-1
            print("list last value is: ",lis1[length]['message'])    
            temp={
                'user':serializer.data,
                'last_message':lis1[length]['message'],
                'time_stamp':lis1[length]['timestamp']
            }
            
            lis.append(temp)
        for users_follower in users_followers:
            check_you_followed= FollowUsers.objects.filter(follower=user, followed=users_follower.follower).first()
            print("123")
            if check_you_followed is None:
                user_follower_data = User.objects.get(id=users_follower.follower.id)
                print(user_follower_data)
                serializer = UserSerializer(user_follower_data)
                # 
                 # 
                current_user= user
                target_chat_user = user_follower_data
                print("hjjjhjh",target_chat_user)
                print(current_user)
                lis1=[]
                threads= Threads.objects.filter(first_person=current_user,second_person=target_chat_user)|Threads.objects.filter(first_person=target_chat_user,second_person=current_user)
                if threads.exists():
                    chatmessages=ThreadChatMessage.objects.filter(thread=threads.first()).order_by('timestamp')
                    for chat_message in chatmessages:
                        serialize= ChatThreadSerializer(chat_message)
                        lis1.append(serialize.data)
                length=len(lis1)-1
                print(length)
                temp_message=''
                temp_timestamp=''
                if length>0:
                    print("list last value is: ",lis1[length]['message']) 
                    temp_message=lis1[length]['message']
                    temp_timestamp=lis1[length]['timestamp']



                temp={
                    'user':serializer.data,
                    'last_message':temp_message,
                    'time_stamp':temp_timestamp
                }
                # 
                lis.append(temp)
        return Response(lis, status=HTTP_200_OK)





