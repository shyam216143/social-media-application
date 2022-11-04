from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from serializers_data.Serializers.TagSerializer import TagSerializer

from my_social_app.models import FollowUsers, Post, Tag, User



class GetTagsView(APIView):
    def get(self,request):
        queryset= Tag.objects.all()
        serializer=TagSerializer(queryset, many=True)
        return Response(serializer.data)
