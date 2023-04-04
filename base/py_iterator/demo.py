import re
import reprlib
from collections import abc
RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come" I say,')

    for word in s:
        print(word)

    print(list(s))

    # python 中x可迭代是因为iter(x)可以返回一个迭代器
    # iter(x) 先尝试调用x.__iter__()获取迭代器
    # 如果x没有实现__iter__()函数，则尝试创建一个迭代器：从索引0开始调用__getitem__(idx)。 这是为了兼容，自己写的时候最好实现__iter__.
    # 如果都没有则触发异常，TypeError: 'xx' object is not iterable
    print(isinstance(s, abc.Iterable))  # 只看__iter__
    print(iter(s))  # 看__iter__和__getitem__

    # 迭代器是这样的对象：实现了无参数的__next__方法，返回序列中的下一个元素；如
    # 果没有元素了，那么抛出StopIteration异常。Python中的迭代器还实现了__iter__
    # 方法，因此迭代器也可以迭代。

    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    print(list(it))  # list() 也会调用迭代器
    print(next(it))  # 元素迭代完了，再调用next会引发StopIteration异常
    # StopIteration异常是迭代完成的标志
