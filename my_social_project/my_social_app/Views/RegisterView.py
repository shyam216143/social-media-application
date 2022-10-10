from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ..serializers import UserRegisterationsSerializer


class UserRegistration(APIView):
    def get(self, request, format=None):
        return Response({'msg': "Success"})

    def post(self, request, format=None):
        serializer = UserRegisterationsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
           
            return Response({
               
                'msg': 'Registration succesfull'
            }, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)