def sorted_squares(nums: list) -> list:
    size = len(nums)
    ret = [0] * size

    i, j, pos = 0, size - 1, size - 1
    while i < j + 1:
        if nums[i] ** 2 > nums[j] ** 2:
            ret[pos] = nums[i] ** 2
            i += 1
        else:
            ret[pos] = nums[j] ** 2
            j -= 1
        pos -= 1

    return ret


def sorted_squares_simple(nums):
    return sorted(x ** 2 for x in nums)
