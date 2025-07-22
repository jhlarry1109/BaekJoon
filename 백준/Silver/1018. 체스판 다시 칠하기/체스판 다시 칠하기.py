n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
w = ['B','W']*4
e = ['W','B']*4
a = []

for i in range(n-7):
    for j in range(m-7):
        c = 0
        for k in range(8):
            for t in range(8):
                if k%2==0:
                    if s[i+k][j:j+8][t] == w[t]:
                        c += 1
                else:
                    if s[i+k][j:j+8][t] == e[t]:
                        c += 1                  
        a.append(c)

for i in range(len(a)):
    a.append(64-a[i])
print(min(a))
