t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    li = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(1, n):
            li[i] += li[i-1]
    print(li[n-1])
