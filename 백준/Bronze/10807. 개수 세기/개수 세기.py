n = int(input())
li = map(int,input().split())
a = int(input())
ans = 0
for i in li:
    if i == a:
        ans += 1
print(ans)