from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..renderers import UserRenderer
from ..serializers import ProfilePhotoSerializer


class UserCoverPhotoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        image = request.data['cover_photo']
        user = request.user
        user.cover_photo = image
        user.save()
        serializer = ProfilePhotoSerializer(user)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)
