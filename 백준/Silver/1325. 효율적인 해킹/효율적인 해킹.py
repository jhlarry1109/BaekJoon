from collections import deque

def bfs(start):
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 1
    
    while q:
        node = q.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)

max_cnt = 0
result = []

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        result = [i]
    elif cnt == max_cnt:
        result.append(i)

print(*result)