# 如何处理不存在的键
# 值是标量时
# d = {
#     'a': 5,
#     's': 3,
#     'd': 8
# }

# key = 'e'
# cnt = -1

# 用in判断
# if key in d:
#     cnt = d[key]
# else:
#     cnt = 0

# 用异常处理
# try:
#     cnt = d[key]
# except KeyError:
#     cnt = 0

# 用get方法
# cnt = d.get(key, 0)

# d[key] = cnt+1

# print(d)

# 值是列表等引用类型时
# counters = {
#     'solar': ['ash', 'firekeeper'],
#     'gewen': ['black knight']
# }

# key = 'salivan'
# who = 'fire knight'

# if key in counters:
#     names = counters[key]
# else:
#     counters[key] = names = []

# try:
#     names = counters[key]
# except KeyError:
#     counters[key] = names = []

# if names := counters.get(key) is None:
#     counters[key] = names = []

# names = counters.setdefault(key, [])

# names.append(who)
# print(counters)

# 使用defauldict处理键缺失情况
from collections import defaultdict

class Visits:
    def __init__(self) -> None:
        # defaultdict的参数是在键缺失时调用的函数，其返回值为对应的value。
        self.data = defaultdict(set)

    def add(self,country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('china', 'beijing')
visits.add('china', 'nanjing')
visits.add('USA', 'LA')
print(visits.data)
