# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 14:08
@desc:
"""

from concurrent.futures import ThreadPoolExecutor
import threading
import time

def action(max):
    sum = 0
    for i in range(max):
        print(threading.current_thread().name+" "+str(i))
        sum += i
    return sum

with ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(action, 50)
    future2 = pool.submit(action, 100)
    def get_result(future):
        print(future.result())
    future1.add_done_callback(get_result)  # 回调函数，线程执行完毕后调用
    future2.add_done_callback(get_result)