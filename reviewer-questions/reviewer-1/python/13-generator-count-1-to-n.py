def count_upto(n):
    for i in range(1, n + 1):
        yield i

for num in count_upto(5):
    print(num)