# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/23 20:07
@desc:
"""

import threading
import time
import Account

# 线程安全错误示例

def draw(account, draw_amount):
    if account.balance >= draw_amount:
        print(threading.current_thread().name+"取钱成功！"+str(draw_amount))
        time.sleep(0.001)
        account.balance -= draw_amount
        print("\t 余额为："+str(account.balance))
    else:
        print(threading.current_thread().name+"取钱失败！余额不足！")

# 创建账户
acct = Account.Account("1234567", 1000)

threading.Thread(name="甲", target=draw, args=(acct, 800)).start()
threading.Thread(name="乙", target=draw, args=(acct, 800)).start()