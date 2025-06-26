from collections import deque

MAX = 100001
n, k = map(int, input().split())
dist = [10**9] * MAX
dist[n] = 0

queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()

    if cur == k:
        break

    if 0 <= 2 * cur < MAX and dist[2 * cur] > dist[cur]:
        dist[2 * cur] = dist[cur]
        queue.appendleft(2 * cur)
        
    for next_pos in [cur - 1, cur + 1]:
        if 0 <= next_pos < MAX and dist[next_pos] > dist[cur] + 1:
            dist[next_pos] = dist[cur] + 1
            queue.append(next_pos)

print(dist[k])
