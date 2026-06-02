def fibonacci(n):
    res = []
    a, b = 0, 1

    for _ in range(n):
        res.append(a)
        a, b = b, a + b

    return res

print(fibonacci(10))