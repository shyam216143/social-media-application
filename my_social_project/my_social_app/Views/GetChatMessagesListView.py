from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from ..models import ThreadChatMessage, Threads

from ..serializers import ChatThreadSerializer, NotificationSerializer


class GetChatMessagesList(APIView):
    def get(self, request):
        current_user = request.user
        target_chat_user = request.GET['target_user']
        lis = []
        threads = Threads.objects.filter(first_person=current_user,
                                         second_person=target_chat_user) | Threads.objects.filter(
            first_person=target_chat_user, second_person=current_user)
        if threads.exists():
            chatmessages = ThreadChatMessage.objects.filter(thread=threads.first()).order_by('timestamp')
            for chat_message in chatmessages:
                serialize = ChatThreadSerializer(chat_message)
                lis.append(serialize.data)
        return Response(lis, status=HTTP_200_OK)
