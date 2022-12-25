import time
from functools import wraps


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
