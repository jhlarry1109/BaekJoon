import heapq

n,m = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}
visited = {i: False for i in range(1,n+1)}
cost = 0
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


pq = []
visited[1] = True

for vertex in graph[1]:
    heapq.heappush(pq, vertex)

while pq:
    c, node = heapq.heappop(pq)
    if not visited[node]:
        cost += c
        visited[node] = True
        for vertex in graph[node]:
            heapq.heappush(pq, vertex)
        
print(cost)