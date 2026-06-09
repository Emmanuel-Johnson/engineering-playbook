import copy

nums = [1, 2, 3, [4, 5, [10, 12], 6], [3, 9]]

print(nums)
print(id(nums))
print(id(nums[3]))

shallow_copy = copy.copy(nums)
deep_copy = copy.deepcopy(nums)

print(shallow_copy)
print(id(shallow_copy))
print(id(shallow_copy[3]))

print(deep_copy)
print(id(deep_copy))
print(id(deep_copy[3]))