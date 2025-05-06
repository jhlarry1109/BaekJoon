n = int(input())
d = [0] * (n + 1)
li = [0] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    li[i] = i - 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
        li[i] = i // 2
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1
        li[i] = i // 3

print(d[n])
d = []
a = n
while a != 0:
    d.append(a)
    a = li[a]
print(*d)