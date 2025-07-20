n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

ranks = [1] * n

for i in range(n):
    for j in range(n):
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            ranks[i] += 1

print(*ranks)
