from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ..models import Countries
from ..renderers import UserRenderer
from ..serializers import ProfileInfoSerializer

#
# class UpdateInfoView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         serializer = ProfileInfoSerializer(data=request.data, context={'user': request.user})
#         if serializer.is_valid(raise_exception=True):
#             return Response({'msg': "profile updated Successfully"}, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        user= request.data
        print("profile user is: ",user)
        serializer = ProfileInfoSerializer(data=request.data, context={'user': request.user})
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print("serializer data is ",serializer.data)
            response= Response()
            response.data=request.data
            response.email=request.user.email

            return response
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

