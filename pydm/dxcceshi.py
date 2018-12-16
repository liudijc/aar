#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time
import a1dmbl
import a2dmcsh
import a3AIdm

def func(name):
    
    if name == "kaiqijc":
        print(a3AIdm.kaiqijc(),name)
    elif name == "ver":
        #print(a3AIdm.dm.ver())
        a3AIdm.jitu_ZJS()



''''
t1 = threading.Thread(target=func,args=("kaiqijc",))
t2 = threading.Thread(target=func,args=("ver",))

t1.start()      # 并发
t2.start()      # 并发

# func("alex")    # 先执行
# func("zingp")   # 再执行
'''