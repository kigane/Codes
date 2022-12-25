from functools import wraps

# 原理
def f1(func):
    def wrapper():
        print('hello')
        func()
        print('bye')
    return wrapper

def f():
    print("This is function f")

f = f1(f) # =wrapper()
# f()

# python 提供的语法糖 @decorator
@f1 # g=f1(g)
def g():
    print("This is function g")

# g()

# 传参和返回值
def f2(func):
    @wraps(func) # 保持返回的包装函数的__name__, __doc__不变
    def wrapper(*args, **kwargs):
        print('f2 hello')
        val = func(*args, **kwargs)
        print('f2 bye')
        return val
    return wrapper

@f2
def h(x, y):
    print(x, y)
    return x + y

print(h(3, 4))



