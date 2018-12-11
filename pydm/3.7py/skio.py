from socketio_client.manager import Manager

import gevent
from gevent import monkey;
monkey.patch_socket()

io = Manager('http', 'localhost', 8000)
chat = io.socket('/chat')

@chat.on_connect()
def chat_connect():
    chat.emit("Hello")

@chat.on('welcome')
def chat_welcome():
    chat.emit("Thanks!")

io.connect()
gevent.wait()