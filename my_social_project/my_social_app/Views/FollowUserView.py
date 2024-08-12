from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import FollowUsers, User
from ..serializers import FollowUsersSerializer, FollowerDataSerializer


class FollowUserView(APIView):
    def post(self, request):
        serializer = FollowUsersSerializer(data=request.data)
        if serializer.is_valid():
            followed_user = User.objects.get(id=request.data['followed'])
            follower_user = User.objects.get(id=request.data['follower'])
            user = FollowUsers.objects.filter(followed=followed_user, follower=follower_user).first()
            if user is None:
                follow = FollowUsers(followed=followed_user, follower=follower_user).save()
                follower_user.following_count = follower_user.following_count + 1
                follower_user.save()
                followed_user.follower_count = followed_user.follower_count + 1
                followed_user.save()
                follower_serializer = FollowerDataSerializer(follower_user)
                return Response({"msg": "Success", "body": follower_serializer.data})
            return Response({"msg": "user already Following"})
        return Response(serializer.errors)
