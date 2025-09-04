def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return
    if parents[x_root] < parents[y_root]:
        parents[x_root] += parents[y_root]
        parents[y_root] = x_root
    else:
        parents[y_root] += parents[x_root]
        parents[x_root] = y_root


n, m = map(int,input().split())
parents = [-1] * (n+1)
for _ in range(m):
    a,x,y = map(int,input().split())
    if a == 0:
        union(x,y)
    else:
        print("YES" if find(x) == find(y) else "NO")