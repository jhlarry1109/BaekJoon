n = int(input())
li = []
for i in range(n):
    li.append(list(map(int,input().split()))[::-1])
li.sort()
for i in li:
    print(*i[::-1])