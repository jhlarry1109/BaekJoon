from collections import deque

n,m = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}
visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(1,0)])
visited[1] = True
li = [(1,0)]
maxedge = 0

while queue:
    node, cnt = queue.popleft()
    if cnt > maxedge:
        maxedge = cnt
        li = [(node, cnt)]
    elif cnt == maxedge:
        li.append((node, cnt))
    for i in graph[node]:
        if not visited[i]:
            queue.append((i, cnt+1))
            visited[i] = True

li.sort()
print(li[0][0], li[0][1], len(li))