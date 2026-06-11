def remove_digits(n):
    if n == 0:
        return

    print(n)
    remove_digits(n // 10)

remove_digits(12345)