# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 14:12
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

with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, (50, 100, 150))   ## 会为每一个元素启动一个线程，并发执行
    print("-----------")
    for r in results:
        print(r)