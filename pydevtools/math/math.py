def add(*nums: int | float) -> int | float:
    total = 0
    for num in nums:
        total = total + num
    return total

def subtract(*nums: int | float) -> int | float:
    if len(nums) != 0:
        total = nums[0]
        for num in nums[1:]:
            total = total - num
        return total
    else:
        return 0

def multiply(*nums: int | float) -> int | float:

    total = 1
    for num in nums:
        total = total * num
    return total

def divide(*nums: int | float) -> int | float:
    if len(nums) != 0:
        total = nums[0] * nums[0]
        for num in nums:
            total = total / num
        return total
    else: 
        return 1
