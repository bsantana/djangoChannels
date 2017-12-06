# In consumers.py
import json
from channels import Group
from channels.sessions import channel_session
from urllib.parse import parse_qs

# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": json.dumps({
            "text": message["text"],
            "username": 'message.channel_session["username"]',
        }),
    })
    obj = json.loads(message["text"])
    obj2 = message["text"]
    print(type(obj))
    print(type(obj2))

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)