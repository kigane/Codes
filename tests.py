import itertools
from datetime import datetime

from icecream import ic

import utils
from leetcode.bucket_sort import *

ic.configureOutput(prefix=lambda: datetime.now().strftime('%H:%M:%S | '),
                   includeContext=False)


def test_bucket_sort():
    ic(max_bits([120, 1230]))

    nums = [1, 2, 4, 5, 23, 12, 7, 36, 97, 4, 325]
    nums_cumsum = list(itertools.accumulate(nums))
    ic(nums_cumsum)
    ic(radix_sort(nums, 0, len(nums)-1, max_bits(nums)))


if __name__ == '__main__':
    test_bucket_sort()
