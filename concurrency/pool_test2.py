# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 16:01
@desc:
"""
import multiprocessing
import time
import os

def action(max):
    sum = 0
    for i in range(max):
        print('(%s)进程正在执行：%d' % (os.getpid(), i))
        sum += i
    return sum

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(action, (50, 100, 150))
        print("-----------")
        for r in results:
            print(r)