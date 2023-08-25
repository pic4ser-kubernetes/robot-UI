from websocket import create_connection
from time import sleep

ws = create_connection('ws://localhost:8000/ws/robot/')

while True:
    print(ws.recv())

ws.close()
