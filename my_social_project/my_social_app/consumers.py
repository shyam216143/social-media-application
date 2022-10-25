from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    # channel_layer = get_channel_layer()
    def websocket_connect(self, event):
        print("websocket is connected..", event)
        print("channel layer is ..", self.channel_layer)
        print("channel name is ..", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            'programmers', self.channel_name)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("websocket is Received..", event['text'])
        print("type of websocket is Received ..", type(event['text']))
        async_to_sync(self.channel_layer.group_send)('programmers', {
            'type': 'chat.message',
            'message': event['text']
        })

    def chat_message(self, event):
        print("event is...", event)
        print("Actual event is...", event['message'])
        print("type of Actual event is...", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print("websocket is disconnected..", event)
        async_to_sync(self.channel_layer.group_discard)(
            'programmers', self.channel_name)
        raise StopConsumer()


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("websocket is connected..", event)
        await  self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("websocket is Received..", event)

    async def websocket_disconnect(self, event):
        print("websocket is disconnected..", event)
        raise StopConsumer()
