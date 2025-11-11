# floyds triangle

num = 1
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()


# pascal's triangle


rows = 5

for i in range(rows):
    print(" " * (rows - i), end="")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)  
    print()


#inverted word pattern

word = "PYTHON"

for i in range(len(word), 0, -1):
    print(word[:i])
