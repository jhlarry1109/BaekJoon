n, k = map(int,input().split())
ans = k
for _ in range(n):
    a, b = map(int,input().split())
    ans += a-b
print('비와이')