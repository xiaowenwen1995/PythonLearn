# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 12:43
@desc:
"""
import threading

# 条件变量练习

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()  # 条件变量
        self._flag = False

    def getBalance(self):
        return self._balance

    def draw(self, draw_amount):
        # 加锁
        self.cond.acquire()
        try:
            if not self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name+"取钱"+str(draw_amount))
                self._balance -= draw_amount
                print("账户余额为："+str(self._balance))
                self._flag = False
                # 唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()

    def deposit(self, deposit_amount):
        # 加锁
        self.cond.acquire()
        try:
            if self._flag:
                self.cond.wait()
            else:
                print(threading.current_thread().name+"存款"+str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为："+str(self._balance))
                self._flag = True
                # 唤醒其他线程
                self.cond.notify_all()
        finally:
            self.cond.release()