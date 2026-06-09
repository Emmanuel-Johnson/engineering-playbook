def second_largest(arr, largest=float('-inf'), second=float('-inf'), index=0):
    if index == len(arr):
        return second

    if arr[index] > largest:
        second = largest
        largest = arr[index]
    elif arr[index] > second and arr[index] < largest:
        second = arr[index]

    return second_largest(arr, largest, second, index + 1)


print(second_largest([5, 4, 6, 3, 9, 2, 0, 1, 7]))