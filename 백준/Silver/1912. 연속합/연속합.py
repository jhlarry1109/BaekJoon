n = int(input())
li = list(map(int,input().split()))
m = li[0]
a = li[0]

for i in range(1, n):
    a = max(a + li[i], li[i])
    m = max(m, a)
print(m)