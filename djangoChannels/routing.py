from channels.routing import route
from exemplo.consumers import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]