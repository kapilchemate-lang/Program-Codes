for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()
n = 1

for i in range(1, 5):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()
for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()
for i in range(1, 6):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
for i in range(5, 0, -1):

    for j in range(5 - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end="")

    print()
n = 5

for i in range(n):
    for j in range(n):

        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
n = 5

for i in range(1, n + 1):
    for j in range(1, i + 1):

        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
num = 1

for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
for i in range(1, 6):
    for j in range(1, i + 1):

        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")

    print()
                                                                