import asyncio
import json
import subprocess
from channels.generic.websocket import AsyncWebsocketConsumer

class ServerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.is_connected = True

    async def disconnect(self, close_code):
        self.is_connected = False

    async def receive(self, text_data):
        print(text_data)
        serv="s1"
        result=f"response from {serv}"
        # command = json.loads(text_data)
        # print(type(command))
        # command=command.get('message')
        try:
            result = subprocess.check_output(text_data, shell=True).decode("utf-8")
        except subprocess.CalledProcessError as e:
            result = str(e)
        print(result)
        
        await self.send(text_data=result)
