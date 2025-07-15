n = int(input())
ans = 0

for i in range(1, n + 1):
    s = i * (i - 1) // 2

    if (n - s) % i == 0 and (n - s) // i >= 1:
        ans += 1

print(ans)
