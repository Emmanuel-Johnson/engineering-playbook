nums = [1, 2, 3, 4, 5]
k = 11

k = k % len(nums)

print(nums[-k:] + nums[:-k])