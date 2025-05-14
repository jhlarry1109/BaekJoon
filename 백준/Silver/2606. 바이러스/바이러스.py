n = int(input())
m = int(input())

graph = {i: [] for i in range(1,n+1)}
visited = {i: False for i in range(1,n+1)}
cnt = 0

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def f(x):
  global cnt
  visited[x] = True
  for node in graph[x]:
    if not visited[node]:
      cnt += 1
      f(node)
      

f(1)
print(cnt)