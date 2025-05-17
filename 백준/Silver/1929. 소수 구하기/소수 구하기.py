m,n = map(int,input().split())
li = []
i = 0
for i in range(n+1):
    li.append(i)
for i in range(2, n):
    if li[i] == 0:
        continue
    for j in range(i*2, n+1, i):
        li[j] = 0
for i in range(n+1):
    if li[i] < m:
        continue
    elif li[i] > n:
        continue
    elif li[i] == 1:
        continue
    print(li[i])