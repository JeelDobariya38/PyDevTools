def add(*nums: int | float) -> int | float:
    total = 0
    for num in nums:
        total = total + num
    return total


def sub(*nums: int | float) -> int | float:
    if len(nums) != 0:
        total = nums[0]
        for num in nums[1:]:
            total = total - num
        return total
    return 0


def mult(*nums: int | float) -> int | float:
    total = 1
    for num in nums:
        total = total * num
    return total


def div(*nums: int | float) -> int | float:
    if len(nums) != 0:
        total = nums[0] * nums[0]
        for num in nums:
            total = total / num
        return total
    return 1


def rem(a: int | float, b: int | float) -> int | float:
    return a % b
