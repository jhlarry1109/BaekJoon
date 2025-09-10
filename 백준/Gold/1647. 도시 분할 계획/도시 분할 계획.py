def find(x):
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return False
    if parents[x_root] < parents[y_root]:
        parents[x_root] += parents[y_root]
        parents[y_root] = x_root
    else:
        parents[y_root] += parents[x_root]
        parents[x_root] = y_root
    return True

n, m = map(int, input().split())
li = []

for _ in range(m):
    a, b, c = map(int, input().split())
    li.append((c, a, b))

li.sort()

parents = [-1] * (n+1)
total = 0
cost = []

for c, a, b in li:
    if union(a, b):
        total += c
        cost.append(c)

print(total - max(cost))
