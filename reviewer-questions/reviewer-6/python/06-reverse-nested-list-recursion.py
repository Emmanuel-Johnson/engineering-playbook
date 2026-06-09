nums = [1,[2,3],[4,5],6] 

def reverse_order(nums, ind=0):
    if ind == len(nums):
        return None
    reverse_order(nums, ind + 1)
    if isinstance(nums[ind], list):
        print(list(reversed(nums[ind])))
    else:
        print(nums[ind])
    
reverse_order(nums)