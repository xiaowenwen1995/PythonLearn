# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 13:18
@desc:
"""

import threading
import Account

def draw_many(account, draw_amount, max):
    for i in range(max):
        account.draw(draw_amount)

def deposit_many(account, deposit_amount, max):
    for i in range(max):
        account.deposit(deposit_amount)

acct = Account.Account("1234567", 0)

threading.Thread(name="取钱者", target=draw_many, args=(acct, 800, 100)).start()
threading.Thread(name="存钱者甲", target=deposit_many, args=(acct, 800, 100)).start()
#threading.Thread(name="存钱者乙", target=deposit_many, args=(acct, 800, 100)).start()
#threading.Thread(name="存钱者丙", target=deposit_many, args=(acct, 800, 100)).start()

# 线程最终被阻塞