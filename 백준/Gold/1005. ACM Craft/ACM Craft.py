t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    d = [0] + list(map(int,input().split()))
    indegree = [0] * (n+1)
    q = []
    dp = [0] * (n+1)
    li = {i:[] for i in range(1, n+1)}
    for i in range(1, k+1):
        x, y = map(int,input().split())
        li[x].append(y)
        indegree[y] += 1
    w = int(input())
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = d[i]
    while q:
        a = q.pop(0)
        for i in li[a]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[a] + d[i])
            if indegree[i] == 0:
                q.append(i)
    print(dp[w])