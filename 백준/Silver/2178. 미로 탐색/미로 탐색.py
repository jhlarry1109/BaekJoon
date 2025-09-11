from collections import deque

n, m = map(int, input().split())
li = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([(0,0)])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1:
            li[nx][ny] = li[x][y] + 1
            queue.append((nx, ny))

print(li[n-1][m-1])