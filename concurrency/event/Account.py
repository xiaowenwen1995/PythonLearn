# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/3/24 13:34
@desc:
"""
import threading

class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.Lock()
        self.event = threading.Event()

    def getBalance(self):
        return self._balance

    def draw(self, draw_amount):
        # 加锁
        self.lock.acquire()
        if self.event.is_set():
            print(threading.current_thread().name+"取钱"+str(draw_amount))
            self._balance -= draw_amount
            print("账户余额为：" + str(self._balance))
            # 内部旗标
            self.event.clear()
            self.lock.release()
            # 阻塞线程
            self.event.wait()
        else:
            self.lock.release()
            self.event.wait()

    def deposit(self, deposit_amount):
        # 加锁
        self.lock.acquire()
        if not self.event.is_set():
            print(threading.current_thread().name+"存款"+str(deposit_amount))
            self._balance += deposit_amount
            print("账户余额为："+str(self._balance))
            # 内部旗标
            self.event.set()
            self.lock.release()
            self.event.wait()
        else:
            self.lock.release()
            self.event.wait()