import time
from timeit import timeit


def sum1(l):
    from itertools import accumulate
    return list(accumulate(l))


def sum2(l):
    from numpy import cumsum
    return list(cumsum(l))


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]

    ret1 = timeit(lambda: sum1(l), number=100000)
    # 0.4243644131347537
    ret2 = timeit(lambda: sum2(l), number=100000)
    print(ret1)
    print(ret2)
    exit()

    start = time.time()  # start time

    time.sleep(5)

    end = time.time()  # 系统绝对时间
    # time.process_time() # 当前进程时间
    # time.thread_time() # 当前线程时间
    m, s = divmod(end-start, 60)
    h, m = divmod(m, 60)
    print("Elapsed time is  {} min {} s".format(m, s))
