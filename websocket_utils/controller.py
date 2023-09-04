import pyglet
import websocket  # https://pypi.org/project/websocket-client/
import json
import threading

# Change this if needed
WEBSOCKET_URL = "ws://localhost:8000/ws/controller/"

controllers = pyglet.input.get_controllers()
print(f"Controllers detected: {controllers}")

if controllers:
    controller = controllers[0]
    print(f"Choosen {controller}.")
    controller.open()


@controller.event
def on_button_press(controller: pyglet.input.Controller, button_name: str):
    print(f"Button {button_name} pressed.")
    ws.send(json.dumps({
        'event': 'button_press',
        'button_name': button_name,
    }))


@controller.event
def on_button_release(controller: pyglet.input.Controller, button_name: str):
    print(f"Button {button_name} released.")
    ws.send(json.dumps({
        'event': 'button_release',
        'button_name': button_name,
    }))


@controller.event
def on_stick_motion(controller: pyglet.input.Controller, stick_name: str, x_value: float, y_value: float):
    print(f"Stick {stick_name} moved to ({x_value}, {y_value}).")
    ws.send(json.dumps({
        'event': 'stick_motion',
        'stick_name': stick_name,
        'x': x_value,
        'y': y_value,
    }))


@controller.event
def on_dpad_motion(controller: pyglet.input.Controller, left: bool, right: bool, up: bool, down: bool):
    print(f"DPad moved to ({left}, {right}, {up}, {down}).")
    ws.send(json.dumps({
        'event': 'dpad_motion',
        'left': left,
        'right': right,
        'up': up,
        'down': down,
    }))


@controller.event
def on_trigger_motion(controller: pyglet.input.Controller, trigger_name: str, value: float):
    print(f"Trigger {trigger_name} moved to {value}.")
    ws.send(json.dumps({
        'event': 'trigger_motion',
        'trigger_name': trigger_name,
        'value': value,
    }))


def on_message(ws, message):
    print(f"Message from websocket: {message}")


def on_error(ws, error):
    print(f"Error websocket: {error}")


def on_close(ws, close_status_code, close_msg):
    print("### closed websocket ###")


def on_open(ws):
    print("Opened websocket connection")
    threading.Thread(target=pyglet.app.run).start()


ws = websocket.WebSocketApp(
    WEBSOCKET_URL,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

ws.run_forever(reconnect=1)
