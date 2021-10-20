def missing_no(nums):
    for i in range(101):
        if i not in nums:
            return i