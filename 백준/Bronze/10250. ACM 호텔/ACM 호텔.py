t = int(input())

for i in range(t):
    H,W,N = map(int,input().split())
    a = 1
    while H < N:
        a += 1
        N -= H
    print("{}".format(N)+"%02d" % a)