from collections import deque

n = int(input())
li = deque([])
l = []

next = 1

for i in range(n):
    k = int(input())

    while k >= next:
        li.append(next)
        next += 1
        l.append('+')

    if li[-1] == k:
        li.pop()
        l.append('-')

    else:
        print('NO')
        exit()
        
for i in l:
    print(i)