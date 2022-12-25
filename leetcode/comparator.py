import random

from icecream import ic


def get_random_array(max_val, max_arr_len):
    # [0, N-1]
    return [random.randint(0, max_val - 1) - random.randint(0, max_val - 1) for _ in range(random.randint(0, max_arr_len))]

def copy_array(arr):
    return arr[:] # list(arr)更可读

def comparator(func1, func2):
    test_times = 10000
    max_val = 1024
    max_arr_len = 100
    success_flag = True
    for _ in range(test_times):
        arr = get_random_array(max_val, max_arr_len)
        arr_copy = copy_array(arr)
        ret1 = func1(arr)
        ret2 = func2(arr_copy)
        if not is_equal(ret1, ret2):
            success_flag = False
            break
            
    return "success!" if success_flag else arr

def is_equal(arr1, arr2):
    for i in range(len(arr1)):
        if (arr1[i] != arr2[i]):
            return False
    return True
    

if __name__ == '__main__':
    nums = get_random_array(10, 20)
    ic(nums)
    ic(id(nums))
    ic(id(copy_array(nums)))

