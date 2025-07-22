n = int(input())
li = []
for i in range(n):
    x, y = input().split()
    li.append([int(x), i, y])
li.sort()
for i in range(n):
    print(li[i][0], li[i][2])