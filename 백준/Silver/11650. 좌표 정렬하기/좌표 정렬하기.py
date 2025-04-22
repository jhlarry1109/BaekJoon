n = int(input())
li = []
result = []
for i in range(n):
    x,y = map(int,input().split())
    li.append([x,y])

li.sort()

for i in range(len(li)):
    print(*li[i])