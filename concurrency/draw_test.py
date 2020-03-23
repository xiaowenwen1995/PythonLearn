# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/23 20:41
@desc:
"""

import threading
import Account

def draw(account, draw_amount):
    account.draw(draw_amount)

acct = Account.Account("1234567", 1000)

threading.Thread(name="甲", target=draw, args=(acct, 800)).start()
threading.Thread(name="乙", target=draw, args=(acct, 800)).start()