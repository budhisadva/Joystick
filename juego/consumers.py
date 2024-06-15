import json
import asyncio
import serial
from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render, redirect

class PantallaConsumidor(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.send_messages_task = asyncio.create_task(self.send_messages())

    async def disconnect(self, close_code):
        self.send_messages_task.cancel()

    async def send_messages(self):
        puerto = '/dev/ttyACM0'     # Aqui cambia el puerto de ser necesario
        pico = serial.Serial(puerto, 9600, timeout=1)
        while True:
            await asyncio.sleep(0.2)
            if pico.in_waiting > 0:
                mensaje = str(pico.readline().decode('UTF-8'))
                await self.send(text_data=json.dumps({
                    'message': mensaje
                }))
