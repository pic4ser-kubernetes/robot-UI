from channels.generic.websocket import AsyncWebsocketConsumer

ROBOT_GROUP = "robot"


class ControllerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        await self.channel_layer.group_send(
            ROBOT_GROUP,
            {
                "type": "robot.message",
                "content": text_data,
            },
        )


class RobotConsumer(AsyncWebsocketConsumer):
    groups = [ROBOT_GROUP]

    async def connect(self):
        await self.accept()

    async def robot_message(self, event):
        await self.send(event["content"])
