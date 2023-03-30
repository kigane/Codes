import itertools


def max_bits(nums: list) -> int:
    max = float('-inf')
    for num in nums:
        if num > max:
            max = num
    bits = 0
    while max != 0:
        max = int(max / 10)
        bits += 1

    return bits


def get_digit(num: int, ind: int):
    """
    获取num从右数第ind位
    """
    while ind > 1:
        num = int(num / 10)
        ind -= 1
    return num % 10


def radix_sort(nums: list, l: int, r: int, digits: int):
    radix = 10
    i = j = 0
    buckets = [0] * (r - l + 1)

    for d in range(1, digits + 1):
        counts = [0] * radix

        # 统计每个数字出现频率
        for i in range(l, r + 1):
            digit = get_digit(nums[i], d)
            counts[digit] += 1

        # 得到排序后每个数字的最后一次出现位置
        counts = list(itertools.accumulate(counts))

        # 频率表转为列表
        for i in reversed(range(l, r + 1)):
            digit = get_digit(nums[i], d)
            if (counts[digit] != 0):
                buckets[counts[digit] - 1] = nums[i]
                counts[digit] -= 1

        # 将数组按某一位的大小排列好
        j = 0
        for i in range(l, r + 1):
            nums[i] = buckets[j]
            j += 1

    return nums


if __name__ == '__main__':
    from icecream import ic

    ic(max_bits([120, 1230]))

    nums = [1, 2, 4, 5, 23, 12, 7, 36, 97, 4, 325]
    nums_cumsum = list(itertools.accumulate(nums))
    ic(nums_cumsum)
    ic(radix_sort(nums, 0, len(nums)-1, max_bits(nums)))
