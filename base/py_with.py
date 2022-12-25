# 原理：with后面的语句被求值后，返回对象的“__enter__()”方法被调用，这个方法的返回值将被赋值给 as 后面的变量
# 当 with 后面的代码块全部被执行完之后，将调用前面返回对象的“__exit__()”方法

class SampleContext():
    def __init__(self) -> None:
        print('初始化')

    def __enter__(self):
        print('我进来了')
        return '打我呀' # foo
    
    # 错误的类型，对应的值，发生的位置
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('我又出去了')



if __name__ == '__main__':
    with SampleContext() as foo:
        print(foo)
    