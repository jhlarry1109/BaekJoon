n = int(input())
li = list(map(int,input().split()))
m = max(li)
ans = 0
for i in range(n):
    ans += li[i] / m * 100
print(ans/n)