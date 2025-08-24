n = int(input())
li = []
ans = 0
a = list(map(int,input().split()))
for i in range(n):
    if a[i] in li:
        ans += 1
    li.append(a[i])
print(ans)