def gen():
    print("prime")
    a = 6
    x = yield a
    print(f"x = {x}")


if __name__ == '__main__':
    it = iter(gen())
    next(it)
    try:
        next(it)
    except StopIteration:
        print("stopped")

    g = gen()
    # next(g)  # 预激活
    g.send(None)  # === next(g)
    try:
        g.send(6)  # send发送的值会成为yield表达式的值
    except StopIteration as ex:
        print(ex.value)
