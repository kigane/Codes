from collections import OrderedDict


class OrderedMeta(type):
    def __init__(cls, name, bases, attrs):
        print(f'cls: {cls}')     # 类
        print(f'name: {name}')   # 类名
        print(f'bases: {bases}') # 继承的基类
        print(f'attrs: {attrs}') # 类属性

    @classmethod # 始终接受一个类对象作为第一个参数，使用Cls.method调用时也会
    # @staticmethod 则在任何时候都不会接收任何隐式参数
    def __prepare__(cls, name, bases):
        '''
            创建attrs字典
        '''
        print('preparing')
        return OrderedDict()

class Example(metaclass=OrderedMeta):
    b = 2
    a = 1
    c = 3
    def __init__(self) -> None:
        self.name = 'lihua'
        self.age = 16
        self.gender = True
        print('Example created')

    def do():
        return 777

if __name__ == '__main__':
   print(Example())
