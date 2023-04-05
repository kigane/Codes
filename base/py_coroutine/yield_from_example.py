from collections import namedtuple

Result = namedtuple("Result", ["count", "average"])

data = {
    'girls;kg': [40.9, 38.5, 44.4, 42.2, 45.2, 52.1, 44.5, 39.1, 40.6, 44.5],
    'girls;m': [1.9, 1.5, 1.4, 1.2, 1.2, 1.1, 1.5, 1.1, 1.6, 1.5],
    'boys;kg': [50.9, 58.5, 54.4, 62.2, 65.2, 52.1, 64.5, 69.1, 70.6, 54.5],
    'boys;m': [1.9, 1.5, 1.6, 1.7, 1.8, 1.7, 1.6, 1.7, 1.6, 1.7],
}


def averager():
    '''子生成器'''
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
    # 返回值会成为grouper函数中yield from表达式的值
    # return会触发StopIteration异常，并将返回值赋给异常的value
    return Result(count, average)


def grouper(results, key):
    '''委派生成器'''
    while True:
        # yield from在子生成器抛出StopIteration会获取其value值并继续运行。
        results[key] = yield from averager()


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print(f'{result.count:2} {group:5} averaging {result.average:.2f} {unit}')


def main(data):
    '''调用方'''
    results = {}
    for k, v in data.items():
        group = grouper(results, k)
        next(group)  # yield from 链条由客户驱动。在最外层委派生成器预激活。
        for val in v:
            group.send(val)  # val会直接send给averager
        # 终止条件，如果没有则yield from调用的协程会永远阻塞。
        # 调用方控制子生成器的终止。子生成器不终止，则委派生成器也会一种阻塞在yield from表达式这里。
        group.send(None)
    print(results)

    report(results)


if __name__ == '__main__':
    main(data)
