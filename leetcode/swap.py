from icecream import ic


def swap(a, b):
    print(id(a))
    print(id(b))
    a ^= b
    print(a)
    print(b)
    b ^= a
    a ^= b
    return a, b

def swap_arr(arr, i, j):
    if (i == j):
        return
    arr[i] ^= arr[j]
    arr[j] ^= arr[i]
    arr[i] ^= arr[j]

if __name__ == '__main__':
    ic(swap(1, 2))
    ic(swap(20124155215, 123))
    a = 1
    b = a
    print(id(a))
    print(id(b))
    ic(swap(a, b))

    nums = [1, 2, 3]
    swap_arr(nums, 1, 1)
    ic(nums)
