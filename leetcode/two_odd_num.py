def two_odd_num(nums):
    eor = 0
    for num in nums:
        eor ^= num
    
    right_one = eor ^ (~eor + 1)

    eor_prime = 0
    for num in nums:
        if num & right_one != 0:
            eor_prime ^= num
    
    print(eor_prime, eor_prime ^ eor)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 66, 66, 66, 77, 77, 89, 89]
    two_odd_num(nums)
