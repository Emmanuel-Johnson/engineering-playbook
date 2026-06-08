def nested_sum(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)   # recursion for nested list
        else:
            total += item

    return total


numbers = [1, 2, [3, 4], [5, [6, 7]], 8]

print(nested_sum(numbers))