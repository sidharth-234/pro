def missing_number(nums):
    n = len(nums) + 1
    total = n * (n + 1) // 2
    return total - sum(nums)

print('oops!! you missed',missing_number([1,2,4,5]))
