def rotate_sn(nums, k):
    ret = []
    n = len(nums)
    for i in range(n):
        ret.append(nums[(i + k) % n])
    # nums = ret # nums只是换了个地址，原nums数组未变
    nums[:] = ret


def rotate_slogk(nums: list, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    要考虑数组长度小于k的情况
    """
    n = len(nums)
    if n == k:
        return
    if n < k:
        k = k % n
    temp = nums[n-k:]
    i = n - 1
    while i > k - 1:
        nums[i] = nums[i - k]
        i -= 1
    while i > -1:
        nums[i] = temp.pop()
        i -= 1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def rotate_s1_1(nums, k):
    """
    i 和 (i + k) / n 交换，从0开始遍历，如果又走到0，且未遍历完，则继续从1开始，如此反复，直到所有元素都遍历一遍为止。
    每次走k步，假设共走了a圈才遍历完。则有 a*n=b*k，于是a*n是n，k的公倍数，当然我们希望a*n取可以取到的最小值，即n，k的最小公倍数lcm(n,k)，则b=lcm(n,k)/k。说明第二次走到起点时，走了b步，访问了b个元素，因此需要n/b次起点+1的操作才能遍历完所有的元素。即n/(lcm(n,k)/k)=nk/lcm(n, k)=gcd(n, k)。
    """
    n = len(nums)
    k = k % n
    count = gcd(n, k)
    for j in range(count):
        prev = nums[j]
        curr = j
        while True:
            next_idx = (curr + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            curr = next_idx
            if curr == j:
                break


def rotate_s1_reverse(nums, k):
    k = k % len(nums)
    nums[:] = nums[::-1]
    nums[:k] = list(reversed(nums[:k]))
    nums[k:] = list(reversed(nums[k:]))
