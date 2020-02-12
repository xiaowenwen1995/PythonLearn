# -*- coding: utf-8 -*- 
"""
@project: PythonLearn
@Author: xiaowenwen 
@time: 2020/2/12 14:09
@desc:
"""


# 闭包函数的实例
# outer是外部函数
def outer(name):
    age = 10  # name,age是局部变量
    # inner是内部函数（嵌套函数）
    def inner():
        # 在内部函数中，用到了外部函数的临时变量
        print("%s今年%d岁了。" % (name, age))

    # 外部函数的返回值是内部函数的引用
    return inner


# 调用外函数传入参数"张三"
# 此时外函数两个临时变量 name是"张三" age是10 ，并创建了内函数，然后把内函数的引用返回存给了person1
# 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
person1 = outer("张三")
# 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
# person1存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
person1()     # 张三今年10岁了。
person2 = outer("李四")
person2()     # 李四今年10岁了。


# 修改闭包变量的实例
# outer是外部函数
def outer(name):
    age = 10  # name,age是局部变量
    # inner是内部函数（嵌套函数）
    def inner():
        # 在内部函数中，用到了外部函数的临时变量
        # 内函数中想修改闭包变量，用nonlocal关键字声明
        nonlocal age
        age = age + 1
        print("%s今年%d岁了。" % (name, age))

    # 外部函数的返回值是内部函数的引用
    return inner


person3 = outer("张三")
person3()     # 张三今年11岁了。
print(person3.__closure__)   # 使用__closure__属性查看闭包变量，返回一个变量元组
person4 = outer("李四")
person4()    # 李四今年11岁了。
print(person4.__closure__)


# 多次调用内部函数时，闭包中的变量相同
def outer(name):
    age = 10  # name,age是局部变量
    # inner是内部函数（嵌套函数）
    def inner():
        # 在内部函数中，用到了外部函数的临时变量
        # 内函数中想修改闭包变量，用nonlocal关键字声明
        nonlocal age
        age = age + 1
        print("%s今年%d岁了。" % (name, age))

    # 外部函数的返回值是内部函数的引用
    return inner


person5 = outer("张三")
person5()    # 李四今年11岁了。
person5()    # 李四今年12岁了。


# 装饰器
def auth(fn):
    def auth_fn(*args):
        print("用一条语句模拟权限检查")
        fn(*args)
    return auth_fn

@auth
def test(a, b):
    print("执行test函数，参数a：%s，参数b：%s" % (a,b))

test(20,15)
"""
输出：
用一条语句模拟权限检查
执行test函数，参数a：20，参数b：15

执行逻辑：
装饰效果相当于auth(test)
test被替换为auth_fn，即执行auth_fn(20,15)
"""


# 单例模式
def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x

    def get_x(self):
        print(self.x)


a1 = A(2)
a2 = A(3)
a1.get_x()  # 2
a2.get_x()  # 2
