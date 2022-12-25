import random
from datetime import datetime

from icecream import ic
from swap import swap_arr

ic.configureOutput(prefix=lambda: datetime.now().strftime('%y-%m-%d %H:%M:%S | '),
                   includeContext=False)


def merge(arr, l, m, r):
    help_arr = [0] * (r - l + 1)
    i = 0
    pl = l
    pr = m + 1
    while pl <= m and pr <= r:
        if arr[pl] < arr[pr]:
            help_arr[i] = arr[pl]
            pl += 1
        else:
            help_arr[i] = arr[pr]
            pr += 1
        i += 1

    while pl <= m:
        help_arr[i] = arr[pl]
        i += 1
        pl += 1

    while pr <= r:
        help_arr[i] = arr[pr]
        i += 1
        pr += 1

    for i in range(len(help_arr)):
        arr[l + i] = help_arr[i]


def merge_sort(arr):
    if arr is None or len(arr) < 2:
        return arr
    process(arr, 0, len(arr)-1)
    return arr


def process(arr, l, r):
    if l == r:
        return
    m = l + ((r - l) >> 1)  # 移位运算优先级比加减低!
    process(arr, l, m)
    process(arr, m + 1, r)
    merge(arr, l, m, r)


def partition(arr, l, r):
    # 将最右值选为pivot，pivot
    pivot = arr[r]
    less_bound = l - 1
    more_bound = r
    i = l
    while i < more_bound:
        if arr[i] < pivot:
            less_bound += 1
            swap_arr(arr, i, less_bound)
            i += 1
        elif arr[i] > pivot:
            more_bound -= 1
            swap_arr(arr, i, more_bound)
        else:
            i += 1
    swap_arr(arr, more_bound, r)
    # 返回=区的左右边界
    # 如果返回less_bound，则所有值都比pivot小的情况下，less_bound为l-1会出错
    return less_bound + 1, more_bound


def quick_sort(arr, l, r):
    if l >= r:
        return

    random_pivot_idx = l + random.randint(0, r - l)
    swap_arr(arr, random_pivot_idx, r)
    less_bound, more_bound = partition(arr, l, r)
    quick_sort(arr, l, less_bound - 1)
    quick_sort(arr, more_bound + 1, r)


def quick_sort_final(arr):
    if arr is None or len(arr) < 2:
        return arr
    quick_sort(arr, 0, len(arr) - 1)
    return arr


def heapify(arr, idx, heap_size):
    """
    保证从idx向下的堆偏序
    """
    left = (idx << 1) + 1

    while left < heap_size:
        largest = left
        if (left + 1) < heap_size:
            largest = left if arr[left] > arr[left+1] else left+1

        largest = idx if arr[idx] > arr[largest] else largest

        if largest == idx:
            break

        swap_arr(arr, idx, largest)

        idx = largest
        left = (idx << 1) + 1


def creat_heap(arr):
    i = (len(arr) - 1) >> 1
    while i >= 0:
        heapify(arr, i, len(arr))
        i -= 1


def heap_insert(arr, idx):
    """
    保证从idx向上的堆偏序
    """
    parent = int((idx - 1) / 2)
    while arr[idx] > arr[parent]:
        swap_arr(arr, idx, parent)
        idx = parent


def heap_sort(arr):
    if arr is None or len(arr) < 2:
        return arr

    heap_size = len(arr)
    # for i in range(heap_size):
    #     heap_insert(arr, i)
    creat_heap(arr)

    heap_size -= 1
    swap_arr(arr, 0, heap_size)
    while heap_size > 0:
        heapify(arr, 0, heap_size)
        heap_size -= 1
        swap_arr(arr, 0, heap_size)

    return arr


if __name__ == '__main__':
    from comparator import comparator

    ret = comparator(heap_sort, sorted)
    ic(ret)
    # nums = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12,
    #         13, 14, 15, 16, 17, 18, 19, 20, 11, 629]
    # print(merge_sort(nums))
    # nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 306, 0, 0, 0, 0, 484, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 785, 0, 0]
    # print(nums)
    # heap_sort(nums)
    # ic(nums)
    # ic(-1 >> 1)  # -1
    # ic(int(-1 / 2))  # 0
