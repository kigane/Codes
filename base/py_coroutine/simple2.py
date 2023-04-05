def coro2(a):
    print("--> a = ", a)
    b = yield a
    print("Recived b = ", b)
    # next(coro) = coro.send(None)
    # yield 右边的表达式会在上一次send后求值，其值会作为send的返回值。
    # yield 左边的变量的值是send发过来的值。
    # yield把右边的值返回给send，把send的参数赋给左边。
    c = yield sum(a, b)
    print("Recived c = ", c)


def sum(a, b):
    print("a + b =", a + b)
    return a + b


if __name__ == '__main__':
    c = coro2(14)
    from inspect import getgeneratorstate
    print(getgeneratorstate(c))  # GEN_CREATED
    m = c.send(None)  # 预激活
    print("m = ", m)
    print(getgeneratorstate(c))  # GEN_SUSPENDED
    m = c.send(28)  # yield收到值，并将其赋值给左边的变量
    print("m = ", m)
    print(getgeneratorstate(c))  # GEN_SUSPENDED
    try:
        c.send(99)  # yield收到值，并将其赋值给左边的变量
    except StopIteration:
        pass
    print(getgeneratorstate(c))  # GEN_CLOSED
