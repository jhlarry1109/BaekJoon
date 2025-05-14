from collections import deque

a,b = map(int,input().split())

def bfs(a, b):
    queue = deque()
    queue.append([a, 1])

    visited = {a:True}

    while queue:
        x, cnt = queue.popleft()
        if x == b:
            return cnt
        if x * 2 <= b and not visited.get(x*2, False):
            visited[x*2] = True
            queue.append([x*2, cnt+1])
        if x * 10 + 1 <= b and not visited.get(x*10+1, False):
            visited[x*10+1] = True
            queue.append([x*10+1, cnt+1])
    return -1
    
print(bfs(a, b))