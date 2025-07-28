max = 100001

prime = [True] * (max+1)
prime[0] = prime[1] = False
for i in range(2, int(max**0.5)+1):
    if prime[i]:
        for j in range(i*i, max+1, i):
            prime[j] = False
primes = [i for i in range(2,max+1) if prime[i]]

def cut(n):
    n = abs(n)
    ans = []
    for i in primes:
        if i*i > n:
            break
        while n%i == 0:
            ans.append(i)
            n //= i
    if n > 1:
        ans.append(n)
    return ans

def up(d, f):
    for i in f:
        d[i] = d.get(i, 0) + 1
    
n = int(input())
li = list(input().split())
a, b = {}, {}
com = 1
zero = 0

for i in range(n*2-1):
    if i%2 != 0:
        if li[i] == '*':
            com = 1
        else:
            com = 0
    else:
        f = cut(int(li[i]))
        if int(li[i]) == 0:
            zero = 1
        if com == 1:
            up(a,f)
        else:
            up(b,f)

if zero:
    print('mint chocolate')
    exit()

for i in b:
    if b[i] > a.get(i, 0):
        print('toothpaste')
        exit()
print('mint chocolate')