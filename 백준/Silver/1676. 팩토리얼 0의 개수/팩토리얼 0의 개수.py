fa = 1
ans = 0
n = int(input())
for i in range(1,n+1):
    fa *= i
fa = str(fa)
for i in fa[::-1]:
    if int(i)%10 != 0:
        break
    ans += 1
print(ans)