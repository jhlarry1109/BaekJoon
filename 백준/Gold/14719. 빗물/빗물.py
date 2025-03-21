h, w = map(int,input().split())
a = list(map(int,input().split()))
x, y = 0, h-1
start = -1
ans = 0
li = []
for i in range(h):
    li.append([])
    for j in range(w):
        li[i].append(0)
for i in a:
    for j in range(i):
        li[y][x] = 1
        y -= 1
    y = h-1
    x += 1
for i in range(h):
    for j in range(w):
        if li[i][j] == 1:
            if start == -1:
                start = j
            else:
                ans += j-start-1
                start = j
    start = -1

print(ans)