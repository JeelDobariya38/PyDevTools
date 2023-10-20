def add(*nums):
    total = 0
    for num in nums:
        total = total + num
    return total


def sub(*nums):
    if len(nums) != 0:
        total = nums[0]
        for num in nums[1:]:
            total = total - num
        return total
    return 0


def mult(*nums):
    total = 1
    for num in nums:
        total = total * num
    return total


def div(*nums):
    if len(nums) != 0:
        total = nums[0] * nums[0]
        for num in nums:
            total = total / num
        return total
    return 1


def rem(a, b):
    return a % b
