def sums(a):
    li = []
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            li.append(s)
    return li

t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

A = sums(a)
B = sums(b)

dict = {}
for i in B:
    dict[i] = dict.get(i,0) + 1

ans = 0
for i in A:
    tg = t-i
    if tg in dict:
        ans += dict[tg]

print(ans)