from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from serializers_data.Serializers.SendPasswordEmailResetSerializer import SendPasswordEmailResetSerializer
from my_social_app.renderers import UserRenderer

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = SendPasswordEmailResetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': "Password Reset lint send. Please Check Your Email"}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)