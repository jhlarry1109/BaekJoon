def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    global count, k, ans
    tmp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= q:
        tmp.append(a[i])
        i += 1
    while j <= r:
        tmp.append(a[j])
        j += 1
    for i in range(len(tmp)):
        a[p + i] = tmp[i]
        count += 1
        if count == k:
            ans = tmp[i]

n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
ans = -1

merge_sort(a, 0, n-1)
print(ans)