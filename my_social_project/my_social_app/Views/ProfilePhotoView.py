from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from ..renderers import UserRenderer
from ..serializers import LoginDataSerializer, ProfilePhotoSerializer
from ..models import User



class UserProfilePhotoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    print("1")
    def post(self, request, id=None):
        print(id)
        serializer = ProfilePhotoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("3")
            image= request.data.get('profile_photo')
            serializer.save()
            user= User.objects.get(id=id)
            user.profile_photo=image
            user.save()
            serializer1=LoginDataSerializer(user, many=False)
            return Response(serializer1.data, status=HTTP_200_OK)

        

       
        return Response(serializer1.error, status=HTTP_400_BAD_REQUEST)