for i in range(1, 6):
    for j in range(1, 10):
        if j >= i and j <= 10 - i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

print()

for i in range(1, 6):
    for j in range(1, 10):
        if j >= i and j <= 10 - i:
            if i % 2 != 0 and j % 2 != 0:
                print("*", end = " ")
            elif i % 2 == 0 and j % 2 == 0:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        else:
            print(" ", end = " ")
    print()
