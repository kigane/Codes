s = "ABCD"

for c in s:
    print(c)

# for in循环的原理
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break
