import websocket

# Change this if needed
WEBSOCKET_URL = "ws://localhost:8000/ws/robot/"


def on_message(ws, message):
    print(f"Message from websocket: {message}")
    # add here code for handling messages


def on_error(ws, error):
    print(f"Error websocket: {error}")


def on_close(ws, close_status_code, close_msg):
    print("### closed websocket ###")


def on_open(ws):
    print("Opened websocket connection")


ws = websocket.WebSocketApp(
    WEBSOCKET_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever(reconnect=1)
