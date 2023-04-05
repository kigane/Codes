from functools import wraps


def corotine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return primer


@corotine
def averager():
    total = 0
    count = 0
    average = 0
    while True:
        x = yield average
        total += x
        count += 1
        average = total / count


if __name__ == '__main__':
    avg = averager()
    # avg.send(None)
    print(avg.send(10))
    print(avg.send(30))
    print(avg.send(5))
