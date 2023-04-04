import re
import reprlib
RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        # return


class SentenceG:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()
        # return


class SentenceGG:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # () 生成器表达式。 返回一个生成器。
        # [] 列表推导。 迭代完，返回拥有所有元素的列表。
        return (m.group() for m in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = SentenceGG('"The time has come" I say,')

    for word in s:
        print(word)

    print(list(s))

    # <generator object <genexpr> at 0x00000247A0A16580>
    print((x for x in 'ABC'))
