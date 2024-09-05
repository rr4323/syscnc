import asyncio
import json
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Subscribe to the "client_group" group
        print("rr")
        serv_name= self.scope['url_route']['kwargs']['serv_name']
        print(serv_name)
        await self.channel_layer.group_add("client_group", self.channel_name)
        self.connection_id = self.scope['path']
        await self.accept()
        self.server_url = settings.REMOTE_NAME_WEBSOCKET_CONNECTION_MAP.get(serv_name)  # Replace with actual server address

        self.server_conn = await websockets.connect(self.server_url)
        self.is_connected = True
        print(self.server_conn)
        

    async def disconnect(self, close_code):
        self.is_connected = False
        await self.server_conn.close()

    async def receive(self, text_data):
        print(text_data)
        if self.is_connected:
            print(self.is_connected)
            await self.server_conn.send(text_data)
            result = await self.server_conn.recv()
            await self.send(text_data=result)
