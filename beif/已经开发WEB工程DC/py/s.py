from socketIO_client import SocketIO, BaseNamespace

def on_response(*args):
    print('on_response', args)

socket = SocketIO('127.0.0.1',3000)
chat = socket.define(BaseNamespace, '/msg')
chat.emit('message')
chat.on('my response', on_response)