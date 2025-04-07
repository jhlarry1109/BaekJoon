n, m = map(int,input().split())
a = []
b = []
ans = []
for _ in range(n):
    a.append(list(map(int,input().split())))
m, k = map(int,input().split())
for _ in range(m):
    b.append(list(map(int,input().split())))
for i in range(n):
    for j in range(k):
        r = 0
        for l in range(m):
            r += a[i][l] * b[l][j]
        ans.append(r)

i = 0
for _ in range(n):
    for _ in range(k):
        print(ans[i],end=' ')
        i += 1
        
    print()