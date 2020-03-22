# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/21 13:25
@desc:
"""

import threading

# 方法
def action(max):
    for i in range(max):
        print(threading.current_thread().getName()+" "+str(i))

# 主线程
for i in range(100):
    print(threading.current_thread().getName()+" "+str(i))
    if i == 20:
        # 子线程1
        t1 = threading.Thread(target=action, args=(100,))
        t1.start()
        # 子线程2
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
print('主线程执行完成！')