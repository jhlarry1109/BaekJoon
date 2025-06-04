n, m = map(int,input().split())
indegree = [0] * (n+1)
q = []
li = {i:[] for i in range(1, n+1)}
for i in range(1, m+1):
    a, b = map(int,input().split())
    li[a].append(b)
    indegree[b] += 1
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
while q:
    x = q.pop(0)
    print(x, end=' ')
    for j in li[x]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)