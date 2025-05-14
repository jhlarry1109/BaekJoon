t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    ans = 0
    idx = m

    while True:
        if q[0] < max(q):
            q.append(q.pop(0))
            if idx == 0:
                idx = len(q) - 1
            else:
                idx -= 1
        else:
            q.pop(0)
            ans += 1
            if idx == 0:
                print(ans)
                break
            else:
                idx -= 1
