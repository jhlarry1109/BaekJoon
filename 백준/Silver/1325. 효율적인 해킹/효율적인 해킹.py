from collections import deque

def bfs(start, graph, n):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 1
    
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_cnt = 0
result = []

for i in range(1, n + 1):
    cnt = bfs(i, graph, n)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

print(*result)