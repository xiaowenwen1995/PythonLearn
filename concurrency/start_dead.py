# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/22 21:10
@desc:
"""

import threading

# 线程只能start一次，对死亡状态的线程再次调用start会报错

def action(max):
    for i in range(100):
        print(threading.current_thread().name+" "+str(i))

sd = threading.Thread(target=action, args=(100,))
for i in range(300):
    print(threading.current_thread().name+" "+str(i))
    if i == 20:
        sd.start()
        print(sd.is_alive())

    if i > 20 and not(sd.is_alive()):
        sd.start()    # 对同一个线程start两次会报错