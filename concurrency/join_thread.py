# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/22 21:35
@desc:
"""
import threading

# 等待另一个线程完成

def action(max):
    for i in range(max):
        print(threading.current_thread().name+" "+str(i))

threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被join的线程")
        jt.start()
        jt.join()  # timeout参数可以设置等待的最长时间
    print(threading.current_thread().name+""+str(i))