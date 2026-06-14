nums = [1, 2, 3, [4, 5, [6, 7], 8], 9, 10]

def flatten(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res
    
print(flatten(nums))