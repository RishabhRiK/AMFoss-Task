# This is a sample code 


import os
import json
import websocket
import threading
import requests
import dotenv

env=dotenv()

TOKEN = os.process.env.BOT_TOKEN
GUILD_ID = "YOUR_GUILD_ID"
CHANNEL_ID = 1412005642562179072

GATEWAY_URL = "wss://gateway.discord.gg/?v=10&encoding=json"

def send_heartbeat(ws, interval):
    import time
    while True:
        ws.send(json.dumps({"op": 1, "d": None}))  # Heartbeat
        time.sleep(interval / 1000)

def on_message(ws, message):
    payload = json.loads(message)

    if payload["op"] == 10:  # Hello packet
        heartbeat_interval = payload["d"]["heartbeat_interval"]
        threading.Thread(target=send_heartbeat, args=(ws, heartbeat_interval)).start()

        # Identify
        identify = {
            "op": 2,
            "d": {
                "token": TOKEN,
                "intents": 513,  # GUILDS + GUILD_MESSAGES
                "properties": {"$os": "linux", "$browser": "my_bot", "$device": "my_bot"}
            }
        }
        ws.send(json.dumps(identify))

    elif payload["t"] == "MESSAGE_CREATE":
        content = payload["d"]["content"]
        author = payload["d"]["author"]["username"]
        print(f"{author}: {content}")

        if content.lower() == "!ping":
            send_message("Pong! 🏓")

def send_message(content):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}
    json_data = {"content": content}
    requests.post(url, headers=headers, json=json_data)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws, close_status_code, close_msg):
    print("Closed connection")

def on_open(ws):
    print("Connected to Gateway")

ws = websocket.WebSocketApp(
    GATEWAY_URL,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
    on_open=on_open
)

ws.run_forever()
