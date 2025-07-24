def gcd(x,y):
    while y != 0:
        x,y = y,x%y
    return x

a,b = map(int,input().split())
msum = 10**9
t = b//a
li = ()
for i in range(1,t):
    if t%i == 0:
        m = i
        n = t//i
        if gcd(m,n) == 1:
            x = a*m
            y = a*n
            if x+y < msum:
                msum = x+y
                li = (min(x,y), max(x,y))
if li:
    print(li[0],li[1])
else:
    print(a,b)