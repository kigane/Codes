from collections import namedtuple

Result = namedtuple("Result", ["count", "average"])
print(Result)


def averager():
    total = 0
    count = 0
    average = 0
    while True:
        x = yield average
        if x == None:
            break
        total += x
        count += 1
        average = total / count
    return Result(count, average)  # 返回值保存到StopIteration对象的value属性


g = averager()
g.send(None)
g.send(10)
g.send(30)
g.send(5)
try:
    g.send(None)
except StopIteration as ex:
    print(ex.value)
