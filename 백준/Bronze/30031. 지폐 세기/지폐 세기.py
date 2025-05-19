n = int(input())
ans = 0
for _ in range(n):
    x,y = map(int,input().split())
    if x == 136:
        ans += 1000
    elif x == 142:
        ans += 5000
    elif x == 148:
        ans += 10000
    elif x == 154:
        ans += 50000
print(ans)