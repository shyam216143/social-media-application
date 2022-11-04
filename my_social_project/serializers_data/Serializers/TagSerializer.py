from rest_framework.serializers import ModelSerializer

from my_social_app.models import User,FollowUsers,Tag

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name', 'dateCreated', 'dateLastModified', 'tagUseCounter', ]
