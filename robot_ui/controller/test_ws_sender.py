from websocket import create_connection
from time import sleep

ws = create_connection('ws://localhost:8000/ws/controller/')
i = 0

while True:
    ws.send(f'test {i}')
    i += 1
    sleep(1)

ws.close()
