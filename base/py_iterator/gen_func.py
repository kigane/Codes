def gen(x):
    for i in range(x):
        yield i


if __name__ == '__main__':
    print(gen)  # function
    print(gen(5))  # generator object

    for i in gen(3):
        print(i)

    g = gen(4)
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    # 生成器函数(函数体中有yield的函数)会创建一个生成器对象，包装生成器函数的定义体。把生成器传给next(...)函数时，生成器函数会向前，执行函数定义体中的下一个yield语句，返回产出的值，并在函数定义体的当前位置暂停。最终，函数的定义体返回时，外层的生成器对象会抛出StopIteration异常——这一点与迭代器协议一致。
