from dataclasses import dataclass, field, FrozenInstanceError
import random
import string

def generate_id():
    return ''.join(random.choices(string.ascii_uppercase, k=12))


class PersonR(object):
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name}, {self.age}'

@dataclass(frozen=True) # 设置frozen=True后，所有实例变量初始化后就不可改变。
class Person(object):
    name: str # dataclass装饰器会将类变量变为实例变量
    age: int = 18 # 提供默认值
    e_mails: list[str] = field(default_factory=list)
    # init=False表示：在生成的__init__方法中不提供id这个关键词参数，即初始化该数据类时不可以用传入的值覆盖该属性。
    id: str = field(init=False, default_factory=generate_id) 
    _search_string: str = field(init=False, repr=False) # 需要用其他传入值组装的可以在__post_init__中处理。repr=False表示不会被打印出来。

    def __post_init__(self):
        ...
        # self._search_string = f'{self.id}-{self.name}'


if __name__ == '__main__':
    p = PersonR(name='levy', age=24)
    print(p)
    pd = Person('jack')
    try:
        pd.age = 44
    except FrozenInstanceError:
        print("Person now immutable!")
    print(pd)