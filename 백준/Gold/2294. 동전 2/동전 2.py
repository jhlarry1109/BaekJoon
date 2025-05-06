n,k = map(int,input().split())
li = []
for i in range(n):
    li.append(int(input()))
d = [100001] * (k+1)
d[0] = 0

for i in li:
    for j in range(i, k+1):
        d[j] = min(d[j], d[j-i] + 1)

if d[k] == 100001:
    print(-1)
else:
    print(d[k])