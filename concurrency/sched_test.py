# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 14:17
@desc:
"""
import sched
import time
import threading

s = sched.scheduler()

def print_time(name='default'):
    print("%s的时间：%s" % (name, time.ctime()))
print('主线程', time.ctime())

# 十秒后执行，优先级为1
s.enter(10, 1, print_time)
# 五秒后执行，优先级为2
s.enter(5, 2, print_time, argument=('位置参数',))
# 五秒后执行，优先级为1
s.enter(5, 1, print_time, kwargs={'name': '关键字参数'})
s.run()
print('主线程', time.ctime())
