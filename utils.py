import time
import timeit
from datetime import datetime
from functools import wraps

from icecream import ic

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)
        end_time = time.time()
        m, s = divmod(end_time-start_time, 60)
        print("Elapsed time is  {} min {} s".format(m, s))
        return val
    return wrapper


def profile(func, number=10000, repeat=1):
    if repeat == 1:
        consumed_time = timeit.timeit(f"{func.__name__}()",
                                      setup=f"from __main__ import {func.__name__}",
                                      number=number)
    else:
        consumed_time = timeit.repeat(f"{func.__name__}()",
                                      setup=f"from __main__ import {func.__name__}",
                                      repeat=repeat,
                                      number=number)
    ic(consumed_time)


def func1():
    x = 0
    while x < 100000:
        x += 1


def func2():
    for x in range(100000):
        pass


if __name__ == '__main__':
    # timeit.timeit(stmt="func1()", setup="", number=1, globals=globals())
    # stmt 为要测试的语句 setup为初始化相关代码
    # number为测试语句执行次数
    # globals为使用的命名空间。如果没有，使用timeit自身的命名空间则无法调用当前文件中定义的函数
    ic(timeit.timeit("func1()", number=1, globals=globals()))
    ic(timeit.timeit("func2()", number=1, globals=globals()))
    # repeat表示重复整个测验的次数
    ic(timeit.repeat("func2()", repeat=3, number=1, globals=globals()))
