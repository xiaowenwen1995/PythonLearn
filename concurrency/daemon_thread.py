# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/23 19:50
@desc:
"""

import threading

def action(max):
    for i in range(max):
        print(threading.current_thread().name+" "+str(i))

t = threading.Thread(target=action, args=(100,), name='后台线程')
t.daemon = True   # 开启后台线程
t.start()
for i in range(10):
    print(threading.current_thread().name+" "+str(i))

# 主程序结束时，后台程序也结束。
