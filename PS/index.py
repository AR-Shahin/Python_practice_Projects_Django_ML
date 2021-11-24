

N = [4, 3, 2, 1]

n = int(''.join(str(i) for i in N))
n += 1
list = []
while n != 0:
    t = n % 10
    list.append(t)
    n = n // 10
list.reverse()
# print(list)

a = ['shain', 'omi', 'ii']

x = "-".join(a)
print(a[0])
