import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class A():
    def __init__(self, msg):
        self.msg = msg

    def foo(self, h):
        time.sleep(1)
        return self.msg

def spider(page, str):
    time.sleep(page)
    return str*10

start = time.time()
# executor = ThreadPoolExecutor(max_workers=4)

# map写法
# i = 1
# for result in executor.map(spider, [2, 3, 1, 4, 1, 1], [2, 3, 1, 4, 1, 1]):
#     print("task{}:{}".format(i, result))
#     i += 1

# submit写法
# future_lst = []
# for el in [2, 3, 5, 6, 4, 1]:
#     future = executor.submit(spider, el, str(el*10))
#     future_lst.append(future)

# for future in as_completed(future_lst):
#     print("task{}".format(future.result()))

foos = [A(str(i)) for i in range(6)]
# 会在最会自动执行executor.shutdown(), 默认是会等待所有结果的。
with ThreadPoolExecutor(max_workers=4) as executor:
    for result in executor.map(foos[0].foo, [None]*6):
        print("task:{}".format(result))