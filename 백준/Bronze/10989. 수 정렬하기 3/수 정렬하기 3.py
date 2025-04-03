n = int(input())
li = [0] * 10001

for i in range(n):
    a = int(input())
    li[a] += 1
for i in range(1, 10001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)