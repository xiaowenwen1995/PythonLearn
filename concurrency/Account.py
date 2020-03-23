# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/23 20:04
@desc:
"""
import threading
import time

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no  # 账户编号
        self._balance = balance        # 账户余额 私有变量
        self.lock = threading.RLock()  # 同步锁

    def getBalance(self):
        return self._balance

    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                print(threading.current_thread().name + "取钱成功！" + str(draw_amount))
                time.sleep(0.001)
                self._balance -= draw_amount
                print("\t 余额为：" + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            # 释放锁
            self.lock.release()
