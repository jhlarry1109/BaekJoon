def sorting():
    seq = []
    queue = []
    for i in range(1,n+1):
        if indeg[i] == 0:
            queue.append(i)
    while queue:
        node = queue.pop(0)
        seq.append(node)
        for i in graph[node]:
            indeg[i] -= 1
            if indeg[i] == 0:
                queue.append(i)

    if len(seq) != n:
        return [0]
    return seq

n, m = map(int,input().split())
indeg = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(m):
    li = list(map(int,input().split()))
    for j in range(1, li[0]):
        a = li[j]
        b = li[j + 1]
        graph[a].append(b)
        indeg[b] += 1

for i in sorting():
    print(i)