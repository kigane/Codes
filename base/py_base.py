import csv

with open('test.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

d = {'a': 1, 'b': 2, 'c': 3}

if 'a' in d:
    print(d.pop('b'))
    print(dir())
