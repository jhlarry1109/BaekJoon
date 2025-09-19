n,m = map(int,input().split())
li = []
for _ in range(n):
    li.append(input()[::-1])
for i in li:
    print(i)