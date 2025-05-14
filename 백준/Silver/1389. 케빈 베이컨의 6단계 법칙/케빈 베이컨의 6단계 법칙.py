from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    queue = deque([x])
    visited = {i: False for i in range(1, n + 1)}
    d = {i: 0 for i in range(1, n + 1)}
    visited[x] = True

    while queue:
        node = queue.popleft()
        for vertex in graph[node]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True
                d[vertex] = d[node] + 1

    return sum(d.values())


min_sum = 5000
answer = 0

for i in range(1, n + 1):
    total = bfs(i)
    if total < min_sum:
        min_sum = total
        answer = i
    elif total == min_sum and i < answer:
        answer = i

print(answer)
