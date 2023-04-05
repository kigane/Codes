from inspect import getgeneratorstate


class DemoException(Exception):
    pass


def co_exception_handle():
    print("co start")
    while True:
        try:
            x = yield
        except DemoException:
            print("DemoException Handled")
        else:
            print(f"coro recieved x = {x}")

    raise RuntimeError("this line will never run")


if __name__ == '__main__':
    g = co_exception_handle()
    print(getgeneratorstate(g))
    g.send(None)
    print(getgeneratorstate(g))
    g.send(10)
    g.throw(DemoException)
    try:
        g.throw(ZeroDivisionError)
    except ZeroDivisionError:
        pass
    print(getgeneratorstate(g))
    try:
        g.send(20)  # 协程中遇到未处理异常后会抛出该异常并终止，再次send会引发Stop Iteration
    except StopIteration:
        pass
    g.close()
    print(getgeneratorstate(g))
