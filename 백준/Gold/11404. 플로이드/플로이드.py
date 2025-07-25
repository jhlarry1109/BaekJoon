n = int(input())
m = int(input())
cost = [[10**9 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    cost[i][i] = 0
    
for i in range(1, m+1):
    a, b, c = map(int,input().split())
    cost[a][b] = min(cost[a][b], c)


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
            
for i in range(1, n+1):
    for j in range(1, n+1):
        if cost[i][j] == 10**9:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()