data = {
    'a': 'hello A',
    'b': 'hello B',
    'c': 'hello C',
    'd': 'hello D',
    'e': 'hello E',
}

result = '{a} -- {c} -- {b}'.format(**data)

print(result)