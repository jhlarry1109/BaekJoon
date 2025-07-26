from collections import deque

n = int(input())
visited = set()
queue = deque()
queue.append((n,0))
visited.add(n)

while queue:
    node,dep = queue.popleft()
    if node == 1:
            print(dep)
            break
    for i in [node//3 if node%3 == 0 else False, node//2 if node%2 == 0 else False, node-1]:
        if i and i not in visited:
            queue.append((i, dep+1))
            visited.add(i)