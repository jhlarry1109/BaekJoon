n = int(input())

li = [1] * (n+1)
li[0] = li[1] = 0
for i in range(2, int(n**0.5) + 1):
    if li[i]:
        for j in range(i*i, n+1, i):
            li[j] = 0

primes = [i for i in range(2, n+1) if li[i]]

start = 0
end = 0
w = 0
ans = 0

while True:
    if w >= n:
        if w == n:
            ans += 1
        w -= primes[start]
        start += 1
    elif end == len(primes):
        break
    else:
        w += primes[end]
        end += 1

print(ans)