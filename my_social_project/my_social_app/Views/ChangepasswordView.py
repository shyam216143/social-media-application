from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ..renderers import UserRenderer

from rest_framework.permissions import IsAuthenticated
from ..serializers import UserChangePasswordSerializer


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, formate=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg': "Password Changed Successfully"}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
