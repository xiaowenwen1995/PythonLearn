# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 15:58
@desc:
"""

import multiprocessing
import time
import os

def action(name='default'):
    print("(%s)进程正在执行，参数为：%s" % (os.getpid(), name))
    time.sleep(3)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)

    pool.apply_async(action)
    pool.apply_async(action, args=('位置参数',))
    pool.apply_async(action, kwds={'name': '关键字参数'})
    pool.close()
    pool.join()