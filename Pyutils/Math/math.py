def sum(*nums: int | float):
    sum = 0
    for num in nums:
        sum += num
    return sum