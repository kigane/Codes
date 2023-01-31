import itertools
from datetime import datetime

from icecream import ic

import utils
from leetcode.bucket_sort import *
from leetcode.comparator import comparator

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


def test_bucket_sort():
    # ic(max_bits([120, 1230]))

    nums = [1, 2, 4, 5, 23, 12, 7, 36, 97, 4, 325]
    # nums_cumsum = list(itertools.accumulate(nums))
    # ic(nums_cumsum)
    radix_sort(nums, 0, len(nums)-1, max_bits(nums))


if __name__ == '__main__':
    # test_bucket_sort()
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # from leetcode.rotate_arr import *
    # rotate_s1_reverse(nums, 3)
    # utils.profile(test_bucket_sort, repeat=5)
    for i in range(1, 5):
        pass
    ic(i)
    a = [1, 2, 5]
    b = [1, 2, 6]
    ic(a == b)
    c = [1, 2, 5]
    ic(a == c)
