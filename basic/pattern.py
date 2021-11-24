n = 5

for i in range(1, n+1):
    sum = 0
    for j in range(1, i+1):
        sum += 1
        if j < 2 or i == sum or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()
