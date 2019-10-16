import time


#  对修改是封闭的，对扩展是开放的

def decorator(func):
    def wrapper(*args, **kwargs):
        print("=============")
        func(*args, **kwargs)

    return wrapper


# 如果有参数则装饰器也需要传入参数

@decorator
def f1(funcc_name):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print('this is a function:' + funcc_name)


@decorator
def f2(funcc_name, funcc_name2):
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print('this is a function:' + funcc_name + "   funcc_name2:" + funcc_name2)


@decorator
def f3(funcc_name, funcc_name2, **kwargs):
    print('this is a function:' + funcc_name + "   funcc_name2:" + funcc_name2)
    print(kwargs)


f1("kkk")
f2("kkk", "ccc")
f3("111", "222", a="aa", b="bb")