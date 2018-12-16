#!/usr/bin/env python
from threading import Lock
import time
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option gased on installed packages.
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
def JSbuju(__id,ZJE,DJLZ):
    danjuLZ=DJLZ.split(",")
    socketio.emit('KHD-buju','pybj',namespace='/test')
    for letter in danjuLZ:     # 第一个实例
        print('当前字母 :', letter,__id)
        socketio.emit('KHD-ZX',letter,namespace=__id)
    socketio.emit('KHD-ZONGjine',ZJE,namespace=__id)
def duqu_zxt():
    f=open("C:/Users/Administrator/Documents/GitHub/aar/pydm/txt/print_zxt.txt","r")
    s=f.read()

    astr=s.split('\n')
    ZXsrt=""
    z=0
    x=0
    h=0
    f.close()
    for i in astr:


        if i=="x":
            x=x+1
            if z != 0:
                ZXsrt=ZXsrt+"Z"+str(z) +","
                z=0
                h=0
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) +","
                z=0
                h=0
        elif i=="z":
            z=z+1
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x) +","
                x=0
                h=0
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) +","
                x=0
                h=0
        elif i=="h":
            h=h+1
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x) +","
                x=0
            elif z !=0:
                ZXsrt=ZXsrt+"Z"+str(z) +","
                z=0
        elif i=="KO":
            if x != 0:
                ZXsrt=ZXsrt+"X"+str(x)
            elif z !=0:
                ZXsrt=ZXsrt+"Z"+str(z) 
            elif h !=0:
                ZXsrt=ZXsrt+"H"+str(h) 
                z=0
                x=0
                h=0
    return ZXsrt
def duqu_zjs():
    f=open("C:/Users/Administrator/Documents/GitHub/aar/pydm/txt/print_zjst.txt","r")
    s=f.read()
    f.close()
    
    return s





'''
def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('KHD-ZONGjine','10',namespace='/test')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)
'''

@socketio.on('my_event', namespace='/test')
def test_message(message):
    print("触发了")
    __id='/test'
    DJLZ=duqu_zxt()
    ZJE="30"
    JSbuju(__id,ZJE,DJLZ)
    print("my_event")

    
    #socketio.emit('KHD-ZX','Z10',namespace='/test')
    #socketio.emit('KHD-ZONGjine','10',namespace='/test')
   
@socketio.on('WY_QRjine', namespace='/test')
def test_WY_QRjine(message):
    print(message)
    
    #socketio.emit('KHD-ZX','Z10',namespace='/test')
    #socketio.emit('KHD-ZONGjine','10',namespace='/test')
   



@socketio.on('connect', namespace='/test')#链接时触发
def test_connect():
    #global thread

    '''
    while i==1:
        DJLZ=duqu_zxt()
        ZJE="30"
        JSbuju(__id,ZJE,DJLZ)
        time.sleep(10) 
    '''       


    #socketio.emit('KHD-buju','Z10',namespace='/test')
    '''
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    '''
    #emit('my_response', {'data': 'Connected', 'count': 0})







if __name__ == '__main__':
    #socketio.run(app, debug=True)
    socketio.run(app,debug=True,host='192.168.1.110',port=5000)
