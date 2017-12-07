from channels.routing import route
from exemplo.consumers import *

channel_routing = [
    route("websocket.connect", ws_add, path=r'^/chat/'),
    route("websocket.receive", ws_message, path=r'^/chat/'),
    route("websocket.disconnect", ws_disconnect, path=r'^/chat/'),

    route('websocket.connect', ws_connect_status, path=r'^/status/'),
    route('websocket.disconnect', ws_disconnect_status, path=r'^/status/'),
    route('websocket.receive', ws_receive_status, path=r'^/status/'),
]