from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..models import User
from ..renderers import UserRenderer
from ..serializers import ProfileInfoSerializer, LoginDataSerializer


class ProfileDataView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        data = User.objects.get(id=id)
        if data is not None:
            serializer1 = LoginDataSerializer(data, many=False)
            response = Response()
            response.data = serializer1.data
            response.followedByAuthUser = 'true'
            print(response.data)
            return response
        return Response({"error": "not a valid id"}, status=HTTP_400_BAD_REQUEST)
