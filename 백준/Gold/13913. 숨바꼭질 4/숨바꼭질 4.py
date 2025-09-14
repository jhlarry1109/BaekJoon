from collections import deque

n,k = map(int,input().split())
visited = [False] * 1000001

queue = deque([(n, 0)])
visited[n] = True
parent = [-1] * 1000001
while queue:
    node, cnt = queue.popleft()
    if node == k:
        print(cnt)
        li = []
        point = k
        while point != -1:
            li.append(point)
            point = parent[point]
        print(*li[::-1])
        break
    for i in (node-1, node+1, node*2):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = True
            queue.append((i, cnt+1))
            parent[i] = node