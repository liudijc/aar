#!/usr/bin/python
#-*-coding:utf-8-*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

while(True):
    data = input("input your data:")
   
    

    socket.send(data.encode('gbk'))

    response = socket.recv()
    print(response.decode('utf8'))